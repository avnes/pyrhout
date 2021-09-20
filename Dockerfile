FROM python:3.9

COPY . sandbox/

WORKDIR sandbox

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN . $HOME/.poetry/env && make install

CMD . $HOME/.poetry/env && make
