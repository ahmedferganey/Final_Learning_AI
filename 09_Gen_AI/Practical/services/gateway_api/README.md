# gateway_api

## Purpose
Service boundary for `gateway_api`.

## Run
```bash
uvicorn services.gateway_api.app.main:app --reload --port 8000
```

## Responsibilities
- own its API contract
- validate inputs
- call shared modules
- expose health checks
