FROM python:3.10-slim

ENV POETRY_VERSION=1.8.3 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

RUN pip install --no-cache-dir poetry==${POETRY_VERSION} \
    && pip install --upgrade --no-cache-dir pip \
    && poetry config virtualenvs.create false 

WORKDIR /project/

COPY poetry.lock pyproject.toml .minio_env /project/
RUN poetry install --only=private_api --no-root --no-directory

COPY /services/private_backend/*.py /project/services/private_backend/
COPY /services/private_backend/src/*.py /project/services/private_backend/src/

WORKDIR /project/services/private_backend/