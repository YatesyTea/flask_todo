# sytax=docker/dockerfile:1

FROM python:3.8-slim

COPY /app /app
RUN pip3 install -r app/requirements.txt
WORKDIR /app

EXPOSE 5000
CMD ["python3", "app.py"]

