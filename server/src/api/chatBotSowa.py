# -*- coding: utf-8 -*-
import os
import sys
import inspect


# Get the current folder, which is the input folder
current_folder = os.path.realpath(
    os.path.abspath(
        os.path.split(
            inspect.getfile(
                inspect.currentframe()
            )
     )[0]
   )
)
folder_parts = current_folder.split(os.sep)
previous_folder = os.sep.join(folder_parts[0:-2])
sys.path.insert(0, current_folder)
sys.path.insert(0, previous_folder)

import json

from flask_restful import Resource,marshal_with, fields ,request, Api



from .customException import CustomException
from .support_jsonp import support_jsonp_custom
from .support_jsonp import support_jsonp_ok
from .support_jsonp import support_jsonp_data

from pymongo import MongoClient


resource_fields = {
    'text':fields.String
}

from chatterbot import ChatBot


from chatterbot.trainers import ListTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance

db_uri=''
strEnvi=""
try:
    strEnvi=os.environ["CHAT_BOT_ENV"]
except Exception as err:
    print("error -> ",err)


#mongodb://mongo:27017/challenge
if (strEnvi=="development"):
    db_uri='mongodb://0.0.0.0:27017',
else:
    db_uri='mongodb://0.0.0.0:27017',


print ("*************** DB -> ", db_uri)

# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://mongo:27017/chatter?readPreference=primary&appname=MongoDB%20Compass&ssl=false'
)


'''
bot = ChatBot(
    'Terminal',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    read_only=True,
    logic_adapters=[
        {
            'import_path':'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatbot.adapters.TemperatureAdapter.TemperatureAdapter',
            'default_response': '...'
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database_uri=db_uri,
    database='local'
    )
'''
#from pymongo import MongoClient
#from pprint import pprint
'''


# -------------------------------------------------------
# Funcion principal 
# -------------------------------------------------------

class ChatBotSowa(Resource,CustomException):
    client = MongoClient(db_uri)
    db=client['chatter']
    def get(self):
        os_env=""
        try:
            usr_input=request.args.get('text')
            bot_output = bot.get_response(usr_input)
            print(" - Chat bot process - ",bot_output);
            
            #
            if (bot_output=='report_list()'):
                r=ChatBotGetReports()
                data=r.get()
                print("Datos List -> ",data)
                return  support_jsonp_data(data)
 
            return support_jsonp_custom({"text":bot_output},resource_fields)
        except Exception as err:
            print("Error ->  ",err);
            return self.showCustomException(err,request.args)
            
class ChatBotTrainSowa(Resource,CustomException):
    def get(self):
        try:
            bot.train("./chatbot/train/")
            return {"train":"ok"}
        except Exception as err:
            return self.showCustomException(err,request.args)

class ChatBotDeleteSowa(Resource,CustomException):
    client = MongoClient(db_uri)
    db=client['chatter']
    statements    = db['statements']
    conversations = db['conversations']

    def get(self):
        try:
            self.statements.remove()
            self.conversations.remove()
            return {"Delete":"ok"}
        except Exception as err:
            return self.showCustomException(err,request.args)

class ChatBotCreateReportListSowa(Resource,CustomException):
    client = MongoClient(db_uri)
    db=client['chatter']
    def get(self):
        try:
            reports = self.db['reports']

            rpt=self.db['reports'].find({"report": "Football" })
            if dumps(rpt, ensure_ascii=False) =="[]":
                reports.insert_one({"report": "Football", "created": datetime.datetime.utcnow()})

            rpt=self.db['reports'].find({"report": "Basketball" })
            if dumps(rpt, ensure_ascii=False) =="[]":
                reports.insert_one({"report": "Basketball", "created": datetime.datetime.utcnow()})

            rpt=self.db['reports'].find({"report": "Tennis" })
            if dumps(rpt, ensure_ascii=False) =="[]":
                reports.insert_one({"report": "Tennis", "created": datetime.datetime.utcnow()})
                
            rpt=self.db['reports'].find({"report": "Golf" })
            if dumps(rpt, ensure_ascii=False) =="[]":
                reports.insert_one({"report": "Golf", "created": datetime.datetime.utcnow()})
                
            rpt=self.db['reports'].find({"report": "Ice Hockey" })
            if dumps(rpt, ensure_ascii=False) =="[]":
                reports.insert_one({"report": "Ice Hockey", "created": datetime.datetime.utcnow()})
                    
            return {"Created":"ok"}
        except Exception as err:
            return self.showCustomException(err,request.args)


class ChatBotGetReports():
    client = MongoClient(db_uri)
    db=client['chatter']
    def get(self):
        try:
            reports = self.db['reports']
            data=self.db['reports'].find()
            data=dumps(data, ensure_ascii=False) 
            
            return data
        except Exception as err:
            return self.showCustomException(err,request.args)



from bson.json_util import dumps
from bson import json_util
import datetime

class ChatBotDBTest(Resource,CustomException):
    client = MongoClient(db_uri)
    db=client['chatter']

    def get(self):
        try:
 
            post = {"author": "Mike",
                    "text": "My first blog post!",
                    "tags": ["mongodb", "python", "pymongo"],
                    "date": datetime.datetime.utcnow()}
            posts = self.db.posts
            post_id = posts.insert_one(post).inserted_id
            print("post_id -> ",post_id)

            cursor = self.db['statements'].find()
            for document in cursor:
                print("type -> ", type(document),document)
          
            return  support_jsonp_data(dumps(self.db['posts'].find(),default=json_util.default))
        except Exception as err:
            return self.showCustomException(err,request.args)
   '''


class ChatBotSowa(Resource,CustomException):
    def get(self):
        try:
            return "TEST"
        except Exception as err:
            print("Error ->  ",err);
             
