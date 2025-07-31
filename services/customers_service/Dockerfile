# ---------- build stage ----------
FROM python:3.12-slim AS builder

# Константы
ENV POETRY_HOME=/opt/poetry \
    POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python - && \
    $POETRY_HOME/bin/poetry config virtualenvs.create false

WORKDIR /srv

COPY ./pyproject.toml ./poetry.lock* ./   
COPY ../../shared_lib ./shared_lib

RUN $POETRY_HOME/bin/poetry install --no-interaction --no-root --only main

# ---------- runtime stage ----------
FROM python:3.12-slim AS runtime

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .
COPY ../../shared_lib ./shared_lib

ENV PORT=8000

CMD ["bash", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
