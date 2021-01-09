from flask_restful import Resource,fields ,request

from api.customException import CustomException
from api.support_jsonp import support_jsonp_data
from api.support_jsonp	import support_jsonp_custom

from api.bot import Bot
from api.bus import Reports

resource_fields = {
    'status':fields.String,
    'message':fields.String
}

from api.data import BotData

class ChatBotDelete(Resource,CustomException):
    def get(self):
        try:
            bot=BotData()
            data=bot.delete()
            return support_jsonp_custom(data,resource_fields)
        except Exception as err:
            return self.showCustomException(err,request.args)
