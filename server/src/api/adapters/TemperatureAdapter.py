from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from datetime import datetime
import requests
import re

class TemperatureAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['what', 'is', 'temperature']
        words1 = ['what', 'is', 'temperature', 'in']
        text=re.sub('[!@#$?]', '', statement.text)
        text=text.lower()
        res= all(x in text.split() for x in words)
        if res:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        try:
            response = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
            data = response.json()
            
            if response.status_code == 200:
                confidence = 1
            else:
                confidence = 0

            temperature =data["main"]["temp"]
            response = Statement('The current temperature is {}'.format(temperature))
            
        except Exception as err:
            confidence = 0
            response = Statement('The current temperature is unavailable')

        response.confidence = confidence
        return response
