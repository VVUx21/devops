FROM python:3.8-alpine

ADD heeloworld.py /tree/heeloworld.py 

CMD [ "python","/tree/heeloworld.py" ]
