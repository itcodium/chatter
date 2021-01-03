# -*- coding: utf-8 -*-

import os
import sys
import inspect

# Get the current folder, which is the input folder
current_folder = os.path.realpath(
    os.path.abspath(
        os.path.split(
            inspect.getfile(
                inspect.currentframe()
            )
     )[0]
   )
)
folder_parts = current_folder.split(os.sep)
previous_folder = os.sep.join(folder_parts[0:-2])
sys.path.insert(0, current_folder)
sys.path.insert(0, previous_folder)



from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
 

db_uri=''
strEnvi=""
try:
    strEnvi=os.environ["CHAT_BOT_SOWA"]
except Exception as err:
    print("error -> ",err)

if (strEnvi=="development"):
    db_uri='mongodb://root:kAUmjz4Hxx36@192.168.220.128:27017',
else:
    db_uri='mongodb://admin:kAUmjz4Hxx36@mongodb:27017',


print ("DB -> ",strEnvi,' - ', db_uri)

chatbot = ChatBot(
    'Terminal',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    read_only=True,
	logic_adapters=[
		{
        	'import_path':'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'adapters.TemperatureAdapter.TemperatureAdapter',
            'default_response': ':)'
        }
    ],

    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],

    database_uri=db_uri,
    database='chatbot'
    )

chatbot.train("./train/")

strInitChat='Iniciando chat';
print(strInitChat)

while True:
    try:
        strInitChat = input()
        res=chatbot.get_response(strInitChat)
        print('Bot: ',res)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
