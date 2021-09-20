.PHONY: run install dev mypy pylint flake8 bandit lint test check docker-test

run:
	poetry run python main.py

install:
	poetry install --no-dev

dev:
	poetry install && poetry run pre-commit install

flake8:
	poetry run flake8 main.py

mypy:
	poetry run mypy main.py

pylint:
	poetry run pylint main.py

bandit:
	poetry run bandit -r main.py

lint:
	$(MAKE) flake8
	$(MAKE) pylint
	$(MAKE) mypy
	$(MAKE) bandit

test:
	poetry run pytest

check:
	poetry run pre-commit run --all-files

docker-test:
	docker build -f Dockerfile-Make .
