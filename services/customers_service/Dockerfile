####################  build stage  ####################
FROM python:3.12-slim AS builder

ENV POETRY_HOME=/opt/poetry \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl  && \
    curl -sSL https://install.python-poetry.org | python - && \
    $POETRY_HOME/bin/poetry config virtualenvs.create false

WORKDIR /srv

# ── 1. общая библиотека ─────────────────────────────
COPY shared_lib /shared_lib

# ── 2. манифесты конкретного сервиса ────────────────
COPY services/customers_service/pyproject.toml .
COPY services/customers_service/poetry.lock* .

# ── 3. ставим runtime-зависимости ───────────────────
RUN $POETRY_HOME/bin/poetry install --no-interaction --no-root --only main

####################  runtime stage  ####################
FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# в PYTHONPATH оставляем только /app
ENV PYTHONPATH="/app:${PYTHONPATH}"

WORKDIR /app

# ── зависимости ─────────────────────────────
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

# ── код сервиса ─────────────────────────────
COPY services/customers_service/app          ./app          
COPY services/customers_service/alembic.ini  ./app/alembic.ini
COPY services/customers_service/migrations   ./app/migrations

# ── shared_lib кладём РЯДОМ, а не в корень FS ──
COPY /shared_lib ./shared_lib              

ENV PORT=8000
CMD ["bash", "-c", "\
     cd app && alembic upgrade head && cd .. && \
     uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]


