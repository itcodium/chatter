
import os
from pymongo import MongoClient
DATABASE='chatter'
class Db():
    client = None
    db=None
    def __init__(self):
        self.client = MongoClient(self.getConection())
        self.db=self.client[DATABASE]
    def getConection(self):
        strEnvi=os.environ["CHAT_BOT_ENV"]
        if (strEnvi=="development"):
            return 'mongodb://mongo:27017/chatter'
        else:
            return  'mongodb://mongo:27017/chatter'