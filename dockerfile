FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
COPY ./requirements.txt /app/requirements.txt

RUN apt update
RUN apt install -y libmagic-dev
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 80
