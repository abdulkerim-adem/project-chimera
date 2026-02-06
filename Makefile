# Chimera Automation Suite
IMAGE_NAME=project-chimera-env

.PHONY: setup test spec-check run-backend

setup:
	pip install -r requirements.txt

test:
	docker build -t $(IMAGE_NAME) .
	docker run --rm $(IMAGE_NAME) python -m pytest tests/

spec-check:
	@echo "🔍 Verifying Spec-Code Alignment..."
	@python scripts/spec_validator.py