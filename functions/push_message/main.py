# coding: utf-8

from ConfigParser import SafeConfigParser

import datetime
import json
import random
import urllib2

from github import Github


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


def get_github_account_info():
    parser = SafeConfigParser()
    parser.read('github.ini')

    username = parser.get('github', 'username')
    password = parser.get('github', 'password')

    return username, password


def get_today_commit_events(user):
    today = datetime.datetime.today()
    today_date = datetime.datetime(today.year, today.month, today.day)
    today_date_ko = today_date - datetime.timedelta(hours=9)

    commit_events = []

    for event in user.get_events():
        if event.created_at > today_date_ko:
            if event.type in ['PushEvent', 'PullRequestEvent']:
                commit_events.append(event)
        else:
            break

    return commit_events


def handle(event, context):
    url = get_slack_incoming_webhook_url()
    username, password = get_github_account_info()

    client = Github(username, password)

    today_commit_events = get_today_commit_events(client.get_user(username))

    if len(today_commit_events) == 0:
        data = {
            'username': bot_name,
            'text': random.choice(message_list)
        }
        data = json.dumps(data)

        req = urllib2.Request(url, data)
        req.add_header('Content-type', 'application/json')

        urllib2.urlopen(req)
