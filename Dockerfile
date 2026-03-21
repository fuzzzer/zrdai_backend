FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV="production" \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir gunicorn uvicorn -r requirements.txt

COPY ./app /app/app
COPY ./entrypoint.sh /app/entrypoint.sh
COPY ./prompts /app/prompts 

RUN mkdir -p /app/storage

RUN chmod +x /app/entrypoint.sh

EXPOSE 8010

ENTRYPOINT ["/app/entrypoint.sh"]