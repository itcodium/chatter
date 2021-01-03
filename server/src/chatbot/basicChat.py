from chatterbot import ChatBot

chatbot = ChatBot(
    'Terminal',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
)

#chatbot.train("./train/")

# Get a response to an input statement
#res=chatbot.get_response("Security threats")
#res=chatbot.get_response("hello")



strInitChat='Iniciando chat';
print(strInitChat)
while True:
    try:
        strInitChat = input()
        res=chatbot.get_response(strInitChat)
        print('Bot: ',res)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
