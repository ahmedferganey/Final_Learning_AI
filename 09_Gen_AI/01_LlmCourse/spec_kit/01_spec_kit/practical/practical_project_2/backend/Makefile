.PHONY: install lint test run

# Install all dependencies including dev extras
install:
	pip install -e ".[dev]"

# Run all linters and type checkers
lint:
	ruff check .
	mypy app/

# Run the test suite (treat empty collection as success for scaffold stage)
test:
	pytest --tb=short -q

# Start the development server
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
