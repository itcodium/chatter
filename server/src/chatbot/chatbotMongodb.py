# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'default_response': 'What can I do for you?.'
        }
    ],

    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database_uri='mongodb://root:kAUmjz4Hxx36@192.168.220.128:27017',
    database='chatter'
)


bot.train("./train/")

strInitChat='Iniciando chat';
print(strInitChat)
while True:
    try:
        bot_output = bot.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
