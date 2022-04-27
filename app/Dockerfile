# syntax=docker/dockerfile:1

# Base image from dockerhub
FROM python:3.10.4-slim-bullseye

# WORKDIR is the directory in the docker's filesystem
WORKDIR /app

# Prepare environment
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# COPY files needed for the app to run
COPY app.py .
COPY ./templates ./templates

# CMD is the command that will run when starting a container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]