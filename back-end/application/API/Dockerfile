
# FROM python:3.7
FROM  jjanzic/docker-python3-opencv

RUN mkdir -p /app

ENV APP_HOME=/app
ENV PYTHONPATH=/app
ENV PORT=8080
ENV CLOUD_STORAGE_BUCKET="the-watcher-storage-file"
# ENV DB_CONN="mysql+pymysql://root:1234567890@localhost:3306/db_watcher"
ENV DB_CONN="mysql+pymysql://root:1234567890@/db_watcher?unix_socket=/cloudsql/imperial-berm-311408:asia-southeast2:the-watchersql"
ENV DB_USER="root"
ENV DB_PASS="1234567890"
ENV DB_NAME="db_watcher"
ENV CLOUD_SQL_CONNECTION_NAME="imperial-berm-311408:asia-southeast2:the-watchersql"


WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ${APP_HOME}

EXPOSE ${PORT}

CMD exec uvicorn --host 0.0.0.0 --port ${PORT} main:app