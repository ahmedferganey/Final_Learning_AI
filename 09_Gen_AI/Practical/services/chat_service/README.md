# chat_service

## Purpose
Service boundary for `chat_service`.

## Run
```bash
uvicorn services.chat_service.app.main:app --reload --port 8001
```

## Responsibilities
- own its API contract
- validate inputs
- call shared modules
- expose health checks
