FROM python:3.11.6-slim-bookworm as poetry_build
LABEL authors="Eremeev Vladimir"
    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.6.1 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/.venv/bin:$PATH"

# prepend poetry and venv to path
RUN python -m venv $POETRY_HOME/.venv && \
    $POETRY_HOME/.venv/bin/python -m pip install poetry==$POETRY_VERSION

# `builder-base` stage is used to build deps + create our virtual environment
FROM poetry_build as ml_filter

WORKDIR /app


COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-interaction --no-cache --without dev
COPY . .
EXPOSE 5000
RUN useradd ml_api_user && chown -R ml_api_user .
USER ml_api_user
CMD [ "poetry", "run", "python", "main.py" ]