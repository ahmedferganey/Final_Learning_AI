# Mini RAG App

Minimal FastAPI service for uploading `.txt` and `.pdf` files, splitting them into chunks with LangChain, and storing project/chunk metadata in MongoDB.

## What Is In This Repo

- `docker/docker-compose.yml`: local MongoDB service
- `src/main.py`: FastAPI app and MongoDB startup/shutdown hooks
- `src/routes/base.py`: base API route
- `src/routes/data.py`: upload and process endpoints
- `src/controllers/`: file validation, project path handling, and content processing
- `src/models/`: MongoDB models, enums, and Pydantic schemas
- `src/assets/mini-rag-app.postman_collection.json`: starter Postman collection

## Current Flow

1. Start MongoDB with Docker Compose.
2. Run the FastAPI app from `src/`.
3. Upload a file to a specific `project_id`.
4. Call the process endpoint with the returned `file_id`.
5. The app reads the file, splits it into chunks, and stores the chunks in MongoDB.

Uploaded files are stored under `src/assets/files/<project_id>/`.

## Requirements

- Python `3.10`
- Docker and Docker Compose
- System packages for Python builds:

```bash
sudo apt update
sudo apt install -y libpq-dev gcc python3-dev
```

## Setup

### 1. Start MongoDB

From the repo root:

```bash
cd docker
cp .env.example .env
```

- update `.env` with your credentials



```bash
docker compose -f docker/docker-compose.yml up -d
```

MongoDB is exposed on `localhost:27007`.





### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r src/requirements.txt
```

### 4. Configure environment variables

Create `src/.env` from `src/.env.example` and fill in the values:

```bash
cp src/.env.example src/.env
```

Recommended values:

```env
APP_NAME=mini-RAG
APP_VERSION=0.1
OPENAI_API_KEY=
FILE_ALLOWED_TYPES=["text/plain","application/pdf"]
FILE_MAX_SIZE=10
FILE_DEFAULT_CHUNK_SIZE=512000
MONGODB_URL=mongodb://localhost:27007
MONGODB_DATABASE=mini_rag
```

Notes:

- `FILE_MAX_SIZE` is in MB.
- `FILE_DEFAULT_CHUNK_SIZE` is the upload write buffer size in bytes.
- The app reads `.env` from inside `src/`, so run the server from `src/` or make sure that file is the active working-directory env file.

## Run The API

From `src/`:

```bash
cd src
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

Base URL:

```text
http://127.0.0.1:8000/api/v1
```

## API Endpoints

### `GET /api/v1/`

Returns the app name and version.

Example response:

```json
{
  "app_name": "mini-RAG",
  "app_version": "0.1"
}
```

### `POST /api/v1/data/upload/{project_id}`

Uploads a file for a project. If the project does not exist in MongoDB yet, it is created automatically.

Request details:

- Path param: `project_id`
- Body type: `form-data`
- File field name: `file`

Example:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/data/upload/demo123" \
  -F "file=@/absolute/path/minirag.txt"
```

Success response:

```json
{
  "signal": "file_upload_success",
  "file_id": "pu8cgha14jj4_minirag.txt",
  "project_id": "demo123"
}
```

Validation errors:

```json
{
  "signal": "file_type_not_supported"
}
```

```json
{
  "signal": "file_size_exceeded"
}
```

### `POST /api/v1/data/process/{project_id}`

Processes a previously uploaded file and stores chunks in MongoDB.

Request body:

```json
{
  "file_id": "pu8cgha14jj4_minirag.txt",
  "chunk_size": 100,
  "overlap_size": 20,
  "do_reset": 0
}
```

Parameters:

- `file_id`: returned by the upload endpoint
- `chunk_size`: chunk length used by `RecursiveCharacterTextSplitter`
- `overlap_size`: overlap between chunks
- `do_reset`: set to `1` to delete previous chunks for the same project before inserting new ones

Example:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/data/process/demo123" \
  -H "Content-Type: application/json" \
  -d '{
    "file_id": "pu8cgha14jj4_minirag.txt",
    "chunk_size": 100,
    "overlap_size": 20,
    "do_reset": 1
  }'
```

Success response:

```json
{
  "signal": "processing_success",
  "inserted_chunks": 42
}
```

Failure response:

```json
{
  "signal": "processing_failed"
}
```

## Postman Upload Issue

If you saw a response like this:

```json
{
  "signal": "file_upload_success",
  "file_id": "pu8cgha14jj4_minirag.txt",
  "project_id": null
}
```

the problem is not with the file itself. The upload API is designed around the path parameter:

```text
/api/v1/data/upload/{project_id}
```

Use a real project id in the URL, for example:

```text
POST http://127.0.0.1:8000/api/v1/data/upload/demo123
```

and send the file as `form-data` using the key `file`.

The server now returns `project_id` explicitly in the upload success payload, so the response should match the project id from the URL.

## Data Model Summary

- `projects` collection:
  - `project_id`
- `chunks` collection:
  - `chunk_text`
  - `chunk_metadata`
  - `chunk_order`
  - `chunk_project_id`

## Supported File Types

The processing controller currently supports:

- `.txt` via `TextLoader`
- `.pdf` via `PyMuPDFLoader`

## Notes

- `project_id` must be alphanumeric based on `src/models/db_schemes/project.py`.
- Uploaded filenames are sanitized and prefixed with a random key before storage.
- The provided Postman collection currently only contains the base welcome request; upload and process requests still need to be added there if you want a complete collection.
