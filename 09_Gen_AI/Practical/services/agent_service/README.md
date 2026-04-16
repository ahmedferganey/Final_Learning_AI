# agent_service

## Purpose
Service boundary for `agent_service`.

## Run
```bash
uvicorn services.agent_service.app.main:app --reload --port 8003
```

## Responsibilities
- own its API contract
- validate inputs
- call shared modules
- expose health checks
