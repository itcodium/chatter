import os
import sys
import inspect
import csv
from flask import request
from flask import Flask
from flask import jsonify 
from flask_restful import Api
from flask_cors import CORS, cross_origin
from flask import abort, redirect, url_for
from flask import Blueprint, render_template

from api import support_jsonp
from api.bus import TestBus
from api.bus import ChatBotBus
from api.bus import TrainBus
#from api import ChatBotDeleteSowa
#from api import ChatBotCreateReportListSowa

current_folder = os.path.realpath(
	os.path.abspath(
		os.path.split(
			inspect.getfile(
				inspect.currentframe()
			)
	)[0]
	)
)

# http://localhost:3001/chatUI/examples/chatbot.html
print("---------------------------------------------")
print("current_folder",current_folder)
print("---------------------------------------------")

application = Flask(__name__, 
	static_url_path='',
	instance_relative_config=True,
	template_folder='templates')

application.jinja_env.add_extension('jinja2.ext.loopcontrols')
main = Blueprint('main', __name__, template_folder='templates')

application.debug = True
application.config['PROPAGATE_EXCEPTIONS'] = True
CORS(application, supports_credentials=True)

@application.route('/test', methods=['GET'])
@support_jsonp
def test():
		return '{"username":"username2017-08-05","email":"test@gmail.com","id":"1597"}'

@application.route('/')
def index():
	return application.send_static_file('index.html')

api = Api(application)
api.add_resource(TestBus, '/api/db')
api.add_resource(ChatBotBus, '/api/chatbot')
api.add_resource(TrainBus, '/api/chatbot/train')
#api.add_resource(ChatBotDeleteSowa, '/api/chatbot/delete')
#api.add_resource(ChatBotCreateReportListSowa, '/api/chatbot/setreport')


if __name__ == "__main__":
	application.run(host='0.0.0.0', port=81)     
