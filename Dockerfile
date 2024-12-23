FROM node:16-alpine

WORKDIR /app

ADD /nodefiles . 
#it will add all the files in the current working directory and put them in the container in the folder tree.
# ADD names.txt .
ENTRYPOINT [ "node" ] 
#execute the command

CMD [ "app.js" ]
