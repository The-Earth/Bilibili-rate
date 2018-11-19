import sqlite3
from vid import getinfo

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