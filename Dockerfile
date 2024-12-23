FROM python:3.8-alpine

WORKDIR /tree

ADD . . 
#it will add all the files in the current working directory and put them in the container in the folder tree.
# ADD names.txt .
ENTRYPOINT [ "python" ] 
#execute the command

CMD [ "heeloworld.py" ]
