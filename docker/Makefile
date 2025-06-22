# .env is expected at the repo root

.DEFAULT_GOAL := help

ENV_FILE := ../.env
DOCKER_COMPOSE := docker-compose -f docker/docker-compose.yml

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

up: ## Start all containers
	$(DOCKER_COMPOSE) up --build -d

down: ## Stop all containers
	$(DOCKER_COMPOSE) down

logs: ## Tail logs from the API
	$(DOCKER_COMPOSE) logs -f api

restart: down up ## Rebuild and restart

bash: ## Open shell in the running container
	docker exec -it agent-bridge-api bash

clean-docker-compose: ## Stop and remove containers/images/volumes by docker-compose project
	docker compose -p agentbridge down --rmi local --volumes
