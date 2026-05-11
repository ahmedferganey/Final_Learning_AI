from fastapi import APIRouter, Depends, UploadFile, status, Request
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProcessController
import aiofiles
from models import ResponseSignal
import logging
from .schemes.data import ProcessRequest
from models.enums.AssetTypeEnum import AssetTypeEnum
from repositories.minirag import ProjectRepository, AssetRepository, ChunkRepository

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(request: Request, project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    # validate the file properties
    data_controller = DataController()

    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )

    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    try:
        async with request.app.db_session_factory() as session:
            project_repository = ProjectRepository(session)
            asset_repository = AssetRepository(session)

            project = await project_repository.get_project_or_create(project_id=project_id)

            await asset_repository.create_asset(
                project_uuid=project.id,
                asset_type=AssetTypeEnum.File.value,
                asset_name=file_id,
                asset_size=os.path.getsize(file_path),
            )

            await session.commit()
    except Exception as exc:
        logger.exception(f"Unable to persist upload metadata: {exc}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    return JSONResponse(
            content={
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id,
                "project_id": project.project_id,
            }   
        )

@data_router.post("/process/{project_id}")
async def process_endpoint(request: Request, project_id: str, process_request: ProcessRequest):

    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size
    do_reset = process_request.do_reset

    try:
        async with request.app.db_session_factory() as session:
            project_repository = ProjectRepository(session)
            asset_repository = AssetRepository(session)
            chunk_repository = ChunkRepository(session)

            project = await project_repository.get_project_or_create(project_id=project_id)
            project_uuid = project.id or await project_repository.get_project_uuid(project_id=project_id)

            if project_uuid is None:
                logger.error(f"Unable to resolve project UUID for project: {project_id}")
                return JSONResponse(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content={
                        "signal": ResponseSignal.PROCESSING_FAILED.value,
                        "project_id": project_id,
                    }
                )

            if file_id is not None:
                project_files_ids = await asset_repository.get_project_asset_by_name(
                    project_uuid=project_uuid,
                    asset_name=file_id,
                    asset_type=AssetTypeEnum.File.value
                )
                if len(project_files_ids) == 0:
                    await session.commit()
                    return JSONResponse(
                        status_code=status.HTTP_404_NOT_FOUND,
                        content={
                            "signal": ResponseSignal.FILE_ID_ERORR.value,
                            "project_id": project_id,
                            "file_id": file_id,
                        }
                    )
            else:
                project_files_ids = await asset_repository.get_all_project_assets(
                    project_uuid=project_uuid,
                    asset_type=AssetTypeEnum.File.value
                )

            if len(project_files_ids) == 0:
                await session.commit()
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "signal": ResponseSignal.FILE_NOT_FOUND.value,
                        "project_id": project_id,
                    }
                )

            process_controller = ProcessController(project_id=project_id)
            if do_reset == 1:
                _ = await chunk_repository.delete_chunks_by_project_uuid(project_uuid=project_uuid)

            inserted_chunks = 0
            processed_files = []
            failed_files = []

            for asset_uuid, current_file_id in project_files_ids.items():
                try:
                    file_content = process_controller.get_file_content(file_id=current_file_id)

                    file_chunks = process_controller.process_file_content(
                        file_content=file_content,
                        file_id=current_file_id,
                        chunk_size=chunk_size,
                        overlap_size=overlap_size
                    )
                except FileNotFoundError as exc:
                    logger.error(f"File not found while processing: {exc}")
                    failed_files.append({
                        "file_id": current_file_id,
                        "signal": ResponseSignal.FILE_NOT_FOUND.value,
                    })
                    continue
                except ValueError as exc:
                    logger.error(f"Invalid file while processing: {exc}")
                    failed_files.append({
                        "file_id": current_file_id,
                        "signal": ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value,
                    })
                    continue
                except Exception as exc:
                    logger.exception(f"Unexpected processing error: {exc}")
                    failed_files.append({
                        "file_id": current_file_id,
                        "signal": ResponseSignal.PROCESSING_FAILED.value,
                    })
                    continue

                if file_chunks is None or len(file_chunks) == 0:
                    failed_files.append({
                        "file_id": current_file_id,
                        "signal": ResponseSignal.PROCESSING_FAILED.value,
                    })
                    continue

                file_chunks_records = [
                    {
                        "chunk_text": chunk.page_content,
                        "chunk_metadata": chunk.metadata,
                        "chunk_order": i + 1,
                        "project_uuid": project_uuid,
                        "asset_uuid": asset_uuid,
                    }
                    for i, chunk in enumerate(file_chunks)
                ]

                inserted_chunks += await chunk_repository.insert_many_chunks(chunks=file_chunks_records)
                processed_files.append(current_file_id)

            await session.commit()

            if len(processed_files) == 0:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        "signal": ResponseSignal.PROCESSING_FAILED.value,
                        "project_id": project_id,
                        "inserted_chunks": inserted_chunks,
                        "processed_files": processed_files,
                        "failed_files": failed_files,
                        "no_files": len(processed_files),
                    }
                )

            return JSONResponse(
                content={
                    "signal": ResponseSignal.PROCESSING_SUCCESS.value,
                    "inserted_chunks": inserted_chunks,
                    "processed_files": processed_files,
                    "failed_files": failed_files,
                    "no_files": len(processed_files),
                }
            )
    except Exception as exc:
        logger.exception(f"Unexpected database processing error: {exc}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "signal": ResponseSignal.PROCESSING_FAILED.value,
                "project_id": project_id,
            }
        )
