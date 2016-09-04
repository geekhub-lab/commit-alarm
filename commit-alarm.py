# coding: utf-8

import json
import random
import urllib2


slack_incoming_webhook_url = \
    'https://hooks.slack.com/services/T00000000/B00000000/000000000000000000000000'
bot_name = 'commit'
message_list = [
    u'커밋좀;',
    u'저기여, 커밋인데여. 오늘 커밋 안하세여?',
    u'커밋은 하고 자야지?',
    u'커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!빼애ㅐㅣ애애애액!!!!!!!!!',
    u'커밋해야 한다(수화기를 들며)',
    u'커밋 컴 윗 미 컴윗',
    u'Make Commit log Great Again',
    u'1 Day 1 Commit (찡긋)'
]

def alarm(event, context):
    data = {
        'username': bot_name,
        'text': random.choice(message_list)
    }
    data = json.dumps(data)

    req = urllib2.Request(slack_incoming_webhook_url, data)
    req.add_header('Content-type', 'application/json')

    urllib2.urlopen(req)
