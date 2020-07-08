FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install django==2.1.4

EXPOSE 8000

COPY . .

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]