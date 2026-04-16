# rag_service

## Purpose
Service boundary for `rag_service`.

## Run
```bash
uvicorn services.rag_service.app.main:app --reload --port 8002
```

## Responsibilities
- own its API contract
- validate inputs
- call shared modules
- expose health checks
