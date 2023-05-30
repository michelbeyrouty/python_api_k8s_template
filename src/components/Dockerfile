FROM python:3.9.4-slim as base
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./src/ .
RUN pip install -r ./components/requirements.txt

FROM base as deployment
RUN rm -rf /tests

FROM base as develop
RUN pip install -r ./components/requirements-dev.txt


