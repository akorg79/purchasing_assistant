FROM python:3.13-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pip setuptools wheel

WORKDIR /app

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels

FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pip --root-user-action=ignore

ENV PYTHONPATH=/app

WORKDIR /app

COPY --from=builder /wheels /wheels

RUN pip install --no-cache-dir /wheels/*

COPY . .

CMD ["python", "app"]
