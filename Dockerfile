FROM python

RUN pip3 install flask --upgrade pip    && \
    pip3 install google-cloud-datastore

COPY ./src src

WORKDIR /src

ENV GOOGLE_APPLICATION_CREDENTIALS datastore-key.json

EXPOSE 5000

CMD ["python","./api.py"]
