
from bson.json_util import dumps
from bson import json_util
import datetime
from pymongo import MongoClient
from flask_restful import Resource
from flask import request
from api.customException import CustomException
from api.support_jsonp import support_jsonp_data
from api.data import Db

class ReportsData(Db):
    def get(self):
        reports = self.db['reports']
        data=self.db['reports'].find()
        data=dumps(data, ensure_ascii=False) 
        return data
