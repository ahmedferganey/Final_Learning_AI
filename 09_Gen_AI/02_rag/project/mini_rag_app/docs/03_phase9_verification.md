# Phase 9 Verification Report

Date: 2026-05-11

## Scope

Phase 8 was intentionally skipped.

Phase 9 verification executed:

- Alembic migration cycle validation (`upgrade -> downgrade -> upgrade`)
- Manual API flow validation (`upload -> process -> index -> search -> rag`)
- PostgreSQL metadata row verification (`projects`, `assets`, `chunks`)

## Alembic Verification

Working directory:

`src/models/db_schemes/minirag`

Commands executed:

```bash
../../../../.venv/bin/python -m alembic -c alembic.ini upgrade head
../../../../.venv/bin/python -m alembic -c alembic.ini downgrade -1
../../../../.venv/bin/python -m alembic -c alembic.ini upgrade head
../../../../.venv/bin/python -m alembic -c alembic.ini current -v
```

Result:

- Migration cycle passed.
- Current revision: `abc25a35ca49 (head)`.

## Manual API Flow

Base endpoint:

```bash
curl -sS http://127.0.0.1:5000/api/v1/
```

Response:

```json
{"app_name":"mini-RAG","app_version":"0.1"}
```

Upload:

```bash
curl -sS -X POST "http://127.0.0.1:5000/api/v1/data/upload/phase9demo" \
  -F "file=@/home/fragello/ME/Github/Learning/Final_Learning_AI/09_Gen_AI/02_rag/project/mini_rag_app/src/assets/files/2/mprohexet682_Ahmed_Ferganey_AI_Platform_Engineer.docx.pdf"
```

Response:

```json
{"signal":"file_upload_success","file_id":"5wg3fh7b04ss_mprohexet682_Ahmed_Ferganey_AI_Platform_Engineer.docx.pdf","project_id":"phase9demo"}
```

Process:

```bash
curl -sS -X POST "http://127.0.0.1:5000/api/v1/data/process/phase9demo" \
  -H "Content-Type: application/json" \
  -d '{"file_id":"5wg3fh7b04ss_mprohexet682_Ahmed_Ferganey_AI_Platform_Engineer.docx.pdf","chunk_size":400,"overlap_size":50,"do_reset":1}'
```

Response:

```json
{"signal":"processing_success","inserted_chunks":20,"processed_files":["5wg3fh7b04ss_mprohexet682_Ahmed_Ferganey_AI_Platform_Engineer.docx.pdf"],"failed_files":[],"no_files":1}
```

Index push:

```bash
curl -sS -X POST "http://127.0.0.1:5000/api/v1/nlp/index/push/phase9demo" \
  -H "Content-Type: application/json" \
  -d '{"do_reset":1}'
```

Response:

```json
{"signal":"insert_into_vectordb_sucess","inserted_items_count":20}
```

Search:

```bash
curl -sS -X POST "http://127.0.0.1:5000/api/v1/nlp/index/search/phase9demo" \
  -H "Content-Type: application/json" \
  -d '{"query_text":"What is this document about?","top_k":3,"limit":3}'
```

Result:

- Response signal: `vectordb_search_success`
- Retrieved 3 hits with `id`, `score`, `text`, and `metadata`.

RAG answer:

```bash
curl -sS -X POST "http://127.0.0.1:5000/api/v1/nlp/rag/answer/phase9demo" \
  -H "Content-Type: application/json" \
  -d '{"question":"Summarize the file","top_k":3,"limit":3,"debug":true}'
```

Result:

- Response signal: `rag_answer_success`
- Returned generated answer plus debug payload and retrieved hits.

## PostgreSQL Row Verification

Command:

```bash
docker exec -i pgvector psql -U postgres -d minirag -c "select project_id,id from projects; select asset_name,project_uuid,id from assets; select count(*) as chunks_for_demo from chunks where project_uuid=(select id from projects where project_id='phase9demo');"
```

Result:

- `projects`: 1 row (`phase9demo`)
- `assets`: 1 row linked to project UUID
- `chunks_for_demo`: 20 rows

## Notes

- No dedicated automated test suite existed in this repo at execution time.
- Phase 9 was completed using migration validation + end-to-end manual API and DB verification.
