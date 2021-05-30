
FROM python:3.7

RUN mkdir -p /app

ENV APP_HOME=/app
ENV PYTHONPATH=/app
ENV PORT=8080
ENV CLOUD_STORAGE_BUCKET="the-watcher-storage-file"
ENV DB_CONN="mysql+pymysql://root:1234567890@localhost:3306/db_watcher"

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ${APP_HOME}

EXPOSE ${PORT}

CMD exec uvicorn --host 0.0.0.0 --port ${PORT} main:app