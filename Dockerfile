FROM python:3.10

WORKDIR /opt/application/

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY src/ src/