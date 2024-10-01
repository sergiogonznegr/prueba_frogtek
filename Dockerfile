FROM python:3.12.5-bullseye

COPY ./requirements.txt /opt/requirements-lint.txt
COPY ./requirements.txt /opt/requirements-dev.txt
COPY ./requirements.txt /opt/requirements.txt
COPY --chown=airflow:root ./src /opt/src

WORKDIR /opt
RUN pip install --no-cache-dir -r /opt/requirements-lint.txt
RUN pip install --no-cache-dir -r /opt/requirements-dev.txt
RUN pip install --no-cache-dir -r /opt/requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/opt/src"