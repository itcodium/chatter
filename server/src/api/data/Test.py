
from bson.json_util import dumps
from bson import json_util
import datetime
from pymongo import MongoClient
from flask_restful import Resource
from flask import request
from api.customException import CustomException
from api.support_jsonp import support_jsonp_data
from api.data import Db

class TestData(Db): 
    def getTest(self):
        self.db['posts'].delete_many({})
        data = {"author": "Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}
        post_id = self.db.posts.insert_one(data).inserted_id
        return self.db['posts'].find()
        