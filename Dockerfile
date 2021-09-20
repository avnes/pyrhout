FROM python:3.9-slim-bullseye

COPY . pyproject.toml sandbox/
COPY . poetry.lock sandbox/
COPY . main.py sandbox/

WORKDIR sandbox

RUN apt update && apt install curl -y

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN . $HOME/.poetry/env && poetry install --no-dev

CMD . $HOME/.poetry/env && poetry run python main.py
