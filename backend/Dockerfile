FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . .

RUN chmod a+x docker/*.sh