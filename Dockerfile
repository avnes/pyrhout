FROM python:3-slim-bullseye

COPY . pyproject.toml sandbox/
COPY . poetry.lock sandbox/
COPY . main.py sandbox/

WORKDIR sandbox

RUN apt update && apt install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN $HOME/.local/bin/poetry install --no-dev

CMD $HOME/.local/bin/poetry run python main.py
