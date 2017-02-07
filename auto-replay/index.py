# -*- encoding=utf-8 -*-
import itchat
import re
from itchat.content import *


@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('.*年.*乐', msg['Text']).span()
    if match:
        itchat.send(('你发的是文字祝福，那我就祝你鸡年大吉吧'), msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    itchat.send(('你发的是picture，暂时不能识别pic上是否有祝福，我还是祝你鸡年大吉吧'), msg['FromUserName'])


itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run(debug=True)
