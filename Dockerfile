
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Allow statements and log messages to immediately appear in the Knative logs
# ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

# RUN pip install ./requirements.txt
COPY ./ /app


RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

EXPOSE 7500
# CMD python3 main.py

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","7500"]

