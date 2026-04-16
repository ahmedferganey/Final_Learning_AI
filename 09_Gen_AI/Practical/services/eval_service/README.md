# eval_service

## Purpose
Service boundary for `eval_service`.

## Run
```bash
uvicorn services.eval_service.app.main:app --reload --port 8004
```

## Responsibilities
- own its API contract
- validate inputs
- call shared modules
- expose health checks
