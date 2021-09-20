# Python Request Headers Output

Simple Flask app to dump all request headers. Useful for debugging.

## Requirements

These software packages must be installed prior to using this repo:

- Python
- poetry

## Usage

This describes how to run the demo code in this project:

```bash
docker pull tagname
docker run -it -p 8080:8080 tagname
curl http://127.0.0.1:8080/
```

## Development

### Virtual environment

```bash
poetry shell
poetry install
make
```

### Linter

```bash
make lint
```

### Install pre-commit hook

The Git pre-commit hook rules are defined in [.pre-commit-config.yaml](.pre-commit-config.yaml)

```bash
poetry shell
pre-commit install
```

### Git check

Check if the code can pass a git pre-commit hook.

```bash
make check
```
