from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from io import BytesIO
from app.api.deps import get_db
from app.db import models
from app.db.crud.qc_data import create_qc_data
import chardet

router = APIRouter()

@router.post("/upload")
async def upload_qc_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only CSV or Excel files are supported")

    try:
        contents = await file.read()

        if file.filename.endswith(".csv"):
            encoding = chardet.detect(contents)["encoding"]
            df = pd.read_csv(BytesIO(contents), encoding=encoding)
        else:
            df = pd.read_excel(BytesIO(contents))

        for _, row in df.iterrows():
            qc_entry = models.qc_data.QCData(
                operator=row["operator"],
                inspector=row["inspector"],
                checker=row["checker"],
                part_number=row["part_number"],
                is_rejected=row["is_rejected"],
                rejection_reason=row.get("rejection_reason"),
                timestamp=pd.to_datetime(row["timestamp"])
            )
            create_qc_data(db, qc_entry)

        return {"message": f"{len(df)} rows uploaded successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
