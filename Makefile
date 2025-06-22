.DEFAULT_GOAL := help

DOCKER_MAKE := $(MAKE) -C docker

help: ## Show this help menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[32m%-20s\033[0m %s\n", $$1, $$2}'

# ───── Docker Shortcuts ─────
up: ## Start API container (via docker makefile)
	$(DOCKER_MAKE) up

down: ## Stop containers
	$(DOCKER_MAKE) down

restart: ## Restart containers
	$(DOCKER_MAKE) restart

logs: ## Tail API logs
	$(DOCKER_MAKE) logs

bash: ## Open shell in container
	$(DOCKER_MAKE) bash

# ───── General Dev Commands ─────
install: ## Install runtime deps
	pip install -r requirements.txt

install-dev: ## Install dev/testing tools
	pip install -r requirements-dev.txt

run-api: ## Run the FastAPI server locally
	uvicorn app.main:app --reload

test: ## Run unit tests
	pytest -v

format: ## Format Python code
	black app tests

lint: ## Lint code with Ruff
	ruff check app tests

clean: ## Remove Python cache, virtualenv, and build artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf venv .venv .tox .eggs *.egg-info

