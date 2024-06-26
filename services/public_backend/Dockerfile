FROM python:3.10-slim

ENV POETRY_VERSION=1.8.3 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

RUN apt update \
    && apt install -y postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir poetry==${POETRY_VERSION} \
    && pip install --upgrade --no-cache-dir pip \
    && poetry config virtualenvs.create false 

WORKDIR /project/

COPY poetry.lock pyproject.toml .psql_env /project/
RUN poetry install --only=public_api --no-root --no-directory

COPY /services/public_backend/*.py /project/services/public_backend/
COPY /services/public_backend/src/*.py /project/services/public_backend/src/
COPY /services/public_backend/src/routers/*.py /project/services/public_backend/src/routers/

WORKDIR /project/services/public_backend/