.PHONY: help install dev lint test format run-gateway run-chat run-rag run-agent run-eval tree

help:
	@echo "install      Install runtime dependencies"
	@echo "dev          Install runtime + dev dependencies"
	@echo "lint         Run ruff"
	@echo "test         Run pytest"
	@echo "run-gateway  Run gateway API"
	@echo "run-chat     Run chat service"
	@echo "run-rag      Run rag service"
	@echo "run-agent    Run agent service"
	@echo "run-eval     Run eval service"

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

lint:
	ruff check .

test:
	pytest -q

run-gateway:
	uvicorn services.gateway_api.app.main:app --reload --port 8000

run-chat:
	uvicorn services.chat_service.app.main:app --reload --port 8001

run-rag:
	uvicorn services.rag_service.app.main:app --reload --port 8002

run-agent:
	uvicorn services.agent_service.app.main:app --reload --port 8003

run-eval:
	uvicorn services.eval_service.app.main:app --reload --port 8004
