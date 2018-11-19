'''遍历全站AID'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

from bilisupport import API_VIDEOSTATUS, HEADERS, APPKEY
import requests
import sqlite3


def getinfo(aid):
    '''
    {comment:'Here is comment',
    {coins: 123,
    ...
    }
    '''
    if not aid:
        return 404
    else:
        aid = int(aid)
    paramsinfo = {'type': 'json', 'appkey': APPKEY, 'id': aid}
    gsvres = requests.get(url=API_VIDEOSTATUS, params=paramsinfo, headers=HEADERS).json()
    if gsvres.get('code') is None:
        postdata = {
            'comment': int(gsvres.get('video_review')),
            'video_review': int(gsvres.get('video_review')),
            'coins': int(gsvres.get('coins')),
            'favorites': int(gsvres.get('favorites')),
            'tid': int(gsvres.get('tid')),
            'typename': str(gsvres.get('typename')),
            'arctype': str(gsvres.get('arctype')),
            'review': int(gsvres.get('review')),
            'title': str(gsvres.get('title')),
            'description': str(gsvres.get('description')),
            'mid': int(gsvres.get('mid')),
        }
        if gsvres.get('play') != "--":
            postdata['play'] = int(gsvres.get('play'))
    else:
        print(aid, gsvres.get('code'), gsvres.get('error'))
        return 404
    return postdata

if __name__ == '__main__':
    for aid in range(36020000, 36020100):
        getinfo(aid)
