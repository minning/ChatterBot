# coding:utf-8
'''
    Author:minning
    Date:2018/1/3
    代码目的：
    
'''

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from prepare import getdata

# chatbot = ChatBot("Training demo")
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.set_trainer(ListTrainer)
chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.chinese")
chatbot.train([
    "嗳，渡边君，真喜欢我?",
    "那还用说?",
    "那么，可依得我两件事?",
    "三件也依得",
])
chatbot.train([
    " 嗯 没的 符号，可以 他给我",
    "嗯 可以啊，您 现在 要 取消 是吗",
    "噢。它 这个 是 怎么 回事 啊，有几天了",
    "对 这边 看到的 话 应该 是 我 看一下 啊！",
])

filepath = '../data/chatPair.csv'
data = getdata(filepath)
chatbot.train(data)

# test
print(chatbot.get_response("真喜欢我?"))
print(chatbot.get_response("可依得我两件事?"))
# print(chatbot.get_response("一定是眼花了"))
# print(chatbot.get_response("先生眨了眨眼"))
# print(chatbot.get_response("你好"))
# print(chatbot.get_response("可以他给我"))
# print(chatbot.get_response("没的符号，可以他"))
# print(chatbot.get_response("可以给我"))
# print(chatbot.get_response("你好"))
print(chatbot.get_response("搞毛线"))
print(chatbot.get_response("学习吧"))
print(chatbot.get_response("带宽很慢"))