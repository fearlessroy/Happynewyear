# -*- encoding=utf-8 -*-
import itchat
import random
import requests
from itchat.content import *

replied = {}


@itchat.msg_register([TEXT])
def text_reply(msg):
    if ('年' or '快乐' or '大吉' in msg['Text']):
        if (msg['FromUserName'] not in replied.keys() or replied[msg['FromUserName']] <= 5):
            sendGreeting(msg)
    else:
        itchat.send(('你发的不是祝福，我还是祝你鸡年大吉吧'), msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    if msg['FromUserName'] not in replied or replied[msg['FromUserName']] <= 5:
        sendGreeting(msg)


def sendGreeting(msg):
    global replied
    friend = itchat.search_friends(userName=msg['FromUserName'])
    itchat.send((friend['RemarkName'] + '，' + getRandomGreeting()), msg['FromUserName'])
    if msg['FromUserName'] not in replied.keys():
        replied[msg['FromUserName']] = 1
    else:
        replied[msg['FromUserName']] += 1


def getRandomGreeting():
    response = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=10",
                            headers={'apiKey': 'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
    results = response.json()['result']
    greetint = results[random.randrange(len(results))]['words']
    return greetint


itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run(debug=True)
