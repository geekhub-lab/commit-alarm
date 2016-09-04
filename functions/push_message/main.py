# coding: utf-8

from ConfigParser import SafeConfigParser

import json
import random
import urllib2


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


def get_slack_incoming_webhook_url():
    parser = SafeConfigParser()
    parser.read('slack.ini')

    return parser.get('slack', 'incoming_webhook_url')


def handle(event, context):
    url = get_slack_incoming_webhook_url()

    data = {
        'username': bot_name,
        'text': random.choice(message_list)
    }
    data = json.dumps(data)

    req = urllib2.Request(url, data)
    req.add_header('Content-type', 'application/json')

    urllib2.urlopen(req)
