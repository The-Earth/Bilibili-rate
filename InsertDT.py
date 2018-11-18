import sqlite3
from bilisupport import API_VIDEOSTATUS, HEADERS, APPKEY
import requests

def InsertData(aid):
    conn = sqlite3.connect('Data.db')
    postdata=getinfo(aid)
    if type(postdata)!=type(1):
        sql = '''insert into Data
                    (VIDEONUMBER,COMMENT,TID,TYPENAME,PLAY,REVIEW,VIDEO_REVIEW,FAVORITES,TITLE,DESCRIPTION,MID,COINS)
                    values(%d,%d,%d,'%s',%d,%d,%d,%d,'%s','%s',%d,%d)''' % (aid,
                                                                            postdata['comment'],
                                                                            postdata['tid'],
                                                                            postdata['typename'],
                                                                            postdata['play'],
                                                                            postdata['review'],
                                                                            postdata['video_review'],
                                                                            postdata['favorites'],
                                                                            postdata['title'],
                                                                            postdata['description'],
                                                                            postdata['mid'],
                                                                            postdata['coins'])
        conn.execute(sql)
        conn.commit()
        conn.close()

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
            'typename': str(gsvres.get('typname')),
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

f=open('AlreadyIn.txt','a')
print("################数据库扩容操作################")
a=int(input('请输入起始视频号'))
b=int(input("请输入终止视频号"))

for i in range(a,b):
    try:
        InsertData(i)
    except:
        pass
print("导入数据完成")
f.write('%d\t%d\n'%(a,b))
f.close()