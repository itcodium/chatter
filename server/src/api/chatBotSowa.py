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
 
 
from Bot import Bot
from pymongo import MongoClient
from pprint import pprint
 
''' 


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


'''