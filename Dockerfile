FROM python:3.12.5-bullseye

COPY ./requirements.txt /opt/requirements.txt
COPY --chown=airflow:root ./src /opt/src

WORKDIR /opt
RUN pip install --no-cache-dir -r /opt/requirements.txt
