FROM  python:3.7
WORKDIR /usr/src/chatter/server
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python3 -m spacy download en
COPY src/ .
EXPOSE 3001
CMD [ "python", "-m chatterbot --version" ] 
CMD [ "python", "./src/server.py" ] 

 
 

 
