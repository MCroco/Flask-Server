FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV FLASK_APP main.py

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY src /usr/src/app/
COPY templates /usr/src/templates
COPY css /usr/src/css

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
