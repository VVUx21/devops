FROM node:16-alpine

ENV BACKEND_URL=http://0.0.0.0:4000

WORKDIR /frontend

ADD . /frontend

RUN npm install

ENTRYPOINT [ "npm" ]

CMD [ "start" ]
