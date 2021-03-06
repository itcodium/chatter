import os
import inspect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Bot:
    bot=None
    name='Terminal'
    logic_adapters=[{'import_path':'chatterbot.logic.BestMatch'},
                    {'import_path':'api.adapters.TemperatureAdapter.TemperatureAdapter'}]
    filters=['chatterbot.filters.RepetitiveResponseFilter']
    def __init__(self):
        self.bot = ChatBot(
            self.name,
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            logic_adapters=self.logic_adapters,
            filters=self.filters,
            database_uri=self.getConection()
        )
    def getConection(self):
        strEnvi=os.environ["CHAT_BOT_ENV"]
        if (strEnvi=="development"):
            return 'mongodb://mongo:27017/chatter',
        else:
            return  'mongodb://mongo:27017/chatter',
    def get(self):
        return self.bot
    def train(self):
        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train("/usr/src/chatter/server/src/api/bot/train")
        return {"status":"ok", "message":  "Train excecuted."}
        