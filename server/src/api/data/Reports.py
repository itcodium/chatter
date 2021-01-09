
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
    def create(self):
        reports = self.db['reports']

        rpt=reports.find({"report": "Football" })
        if dumps(rpt, ensure_ascii=False) =="[]":
            reports.insert_one({"report": "Football", "created": datetime.datetime.utcnow()})

        rpt=reports.find({"report": "Basketball" })
        if dumps(rpt, ensure_ascii=False) =="[]":
            reports.insert_one({"report": "Basketball", "created": datetime.datetime.utcnow()})

        rpt=reports.find({"report": "Tennis" })
        if dumps(rpt, ensure_ascii=False) =="[]":
            reports.insert_one({"report": "Tennis", "created": datetime.datetime.utcnow()})
            
        rpt=reports.find({"report": "Golf" })
        if dumps(rpt, ensure_ascii=False) =="[]":
            reports.insert_one({"report": "Golf", "created": datetime.datetime.utcnow()})
            
        rpt=reports.find({"report": "Ice Hockey" })
        if dumps(rpt, ensure_ascii=False) =="[]":
            reports.insert_one({"report": "Ice Hockey", "created": datetime.datetime.utcnow()})
        
        return {"status":"ok", "message":"Se ejecuto la creacion del reporte."}                
