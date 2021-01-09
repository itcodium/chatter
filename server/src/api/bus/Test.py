from bson.json_util import dumps
from bson import json_util
from flask_restful import Resource,fields ,request

from api.customException import CustomException
from api.support_jsonp import support_jsonp_data

resource_fields = {
    'text':fields.String
}

from api.data import TestData          

class TestBus(Resource,CustomException):
    def get(self):
        try:
            test=TestData()
            return  support_jsonp_data(dumps(test.getTest(),default=json_util.default))
        except Exception as err:
            return self.showCustomException(err,request.args)
