FROM python:latest
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

