FROM python:3.8-alpine

ADD ./requirements.txt /backend/requirements.txt

RUN pip install -r /backend/requirements.txt

ADD . /backend

WORKDIR /backend

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
