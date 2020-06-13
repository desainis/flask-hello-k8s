FROM python:3.8.3-alpine3.12

RUN apk update

COPY ./requirements.txt /app/requirements.txt

COPY ./harden.sh /app/harden.sh

WORKDIR /app

RUN chmod +x ./harden.sh
RUN ./harden.sh

RUN pip install -r requirements.txt

COPY . /app
ENV FLASK_APP=hello.py
CMD ["python3", "hello.py"]
