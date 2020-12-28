FROM  python:3.8
WORKDIR /usr/src/chatter/server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 3001
CMD [ "python", "./server.py" ] 

 
 
