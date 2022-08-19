FROM python:3.9-slim

WORKDIR /opt/application/

COPY requeriments.txt .
COPY .env .

RUN pip install -r requeriments.txt

COPY src/ src/

COPY migrations/ migrations/

COPY alembic.ini .



