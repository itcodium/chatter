from flask_restful import Resource,fields ,request

from api.customException import CustomException
from api.support_jsonp import support_jsonp_data
from api.support_jsonp	import support_jsonp_custom

from api.bot import Bot
from api.data import ReportsData

resource_fields = {
    'status':fields.String,
    'message':fields.String
}

class ReportsCreateBus(Resource,CustomException):
    def get(self):
        try:
            report=ReportsData()
            data=report.create ()
            return support_jsonp_custom(data,resource_fields)
        except Exception as err:
            return self.showCustomException(err,request.args)
