from flask_restful import Resource,fields ,request

from api.customException import CustomException
from api.support_jsonp import support_jsonp_data
from api.support_jsonp	import support_jsonp_custom

from api.bot import Bot
from api.bus import Reports

resource_fields = {
    'text':fields.String
}

class TrainBus(Resource,CustomException):
    def get(self):
        try:
            bot = Bot()
            result=bot.train()
            return support_jsonp_custom({"text":result},resource_fields)
        except Exception as err:
            return self.showCustomException(err,request.args)
