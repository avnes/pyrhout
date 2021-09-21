FROM python:3.9-alpine

COPY . pyproject.toml sandbox/
COPY . poetry.lock sandbox/
COPY . main.py sandbox/

WORKDIR sandbox

RUN apk update && apk add curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN . $HOME/.poetry/env && poetry install --no-dev

CMD . $HOME/.poetry/env && poetry run python main.py
