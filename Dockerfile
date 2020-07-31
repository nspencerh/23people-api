FROM python:alpine3.7

RUN pip3 install flask

COPY ./src src

WORKDIR /src

EXPOSE 5000

CMD ["python","./api.py"]
