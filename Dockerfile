# local環境用のDockerfile

FROM python:3.9.6

RUN apt-get update -y

RUN apt-get install -y sqlite3

RUN sqlite3 testdb.sqlite3

RUN ls

COPY ./src /var/app/test-fastapi/src

COPY ./requirements.txt /var/app/test-fastapi/requirements.txt

RUN pip install -r /var/app/test-fastapi/requirements.txt

WORKDIR /var/app/test-fastapi

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80", "--app-dir", "./src/api"]
