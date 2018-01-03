# coding:utf-8
'''
    Author:minning
    Date:2018/1/2
    代码目的：两个聊天机器人进行自动聊天，会擦出什么样的火花呢
    chatbot 1 ：https://github.com/sohelamin/chatbot
    chatbot 2 ：https://github.com/gunthercox/ChatterBot
    
'''
import aiml
import os
from chatterbot import ChatBot

chatbot1 = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    chatbot1.bootstrap(brainFile="bot_brain.brn")
else:
    chatbot1.bootstrap(learnFiles=os.path.abspath("aiml/std-startup.xml"), commands="load aiml b")
    chatbot1.saveBrain("bot_brain.brn")

chatbot2 = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
# chatbot2.train("chatterbot.corpus.english")

message = 'how old are you'
print "chatbot 2 : {}".format(message)
while True:
    if message == "quit":
        exit()
    elif message == "save":
        chatbot1.saveBrain("bot_brain.brn")
    else:
        chat1 = chatbot1.respond(message)
        print "chatbot 1 : {}".format(chat1)
        chat2 = chatbot2.get_response(chat1)
        print "chatbot 2 : {}".format(chat2)
        # print type(str(chat2))
        message = str(chat2)
