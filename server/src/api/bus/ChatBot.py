from flask_restful import Resource,fields ,request

from api.customException import CustomException
from api.support_jsonp import support_jsonp_data
from api.support_jsonp	import support_jsonp_custom

from api.bot import Bot
from api.bus import Reports

resource_fields = {
    'text':fields.String
}

class ChatBotBus(Resource,CustomException):
    bot = Bot().get()
    report=Reports()
    def get(self):
        try:
            usr_input=request.args.get('text')
            bot_output = self.bot.get_response(usr_input)
            print(" =============  ChatBotBus process - ",usr_input, " - ",bot_output)
            if (bot_output=='report_list()'):
                data=self.report.get()
                return  support_jsonp_data(data)
            return support_jsonp_custom({"text":bot_output},resource_fields)
        except Exception as err:
            return self.showCustomException(err,request.args)
