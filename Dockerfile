FROM node:20.7.0 as npm
COPY package-lock.json . /app/
COPY package.json . /app/
WORKDIR /app/
RUN npm install package.json

FROM python:3.11.5 as django
COPY . /app/
WORKDIR /app/


ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt


