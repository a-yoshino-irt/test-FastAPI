# local環境用のDockerfile

FROM python:3.9.6

RUN apt-get update -y

RUN apt-get install -y sqlite3

COPY ./api /var/app/test-fastapi/api

COPY ./requirements.txt /var/app/test-fastapi/requirements.txt

RUN pip install -r /var/app/test-fastapi/requirements.txt

WORKDIR /var/app/test-fastapi

RUN sqlite3 test_fastapi.sqlite3

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80", "--app-dir", "./api"]
