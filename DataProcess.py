import sqlite3
import vid
import math

def Builtdatabase():
    conn = sqlite3.connect('Data.db')
    # 创建数据表Data
    sql1 = '''CREATE TABLE Data(
                    VIDEONUMBER INTERGER    PRIMARY KEY     NOT NULL,
                    COMMENT     INTERGER    NOT NULL,
                    TID         INTERGER    NOT NULL,
                    PLAY        INTERGER    NOT NULL,
                    REVIEW      INTERGER    NOT NULL,
                    VIDEO_REVIEW    INTERGER    NOT NULL,
                    FAVORITES   INTERGER    NOT NULL,
                    MID         INTERGER    NOT NULL,
                    COINS       INTERGER    NOT NULL,
                    YTRAIN      INTERGER    NOT NULL,
                    TITLE       TEXT        NOT NULL,
                    TYPENAME    TEXT        NOT NULL,
                    DESCRIPTION TEXT        NOT NULL);'''
    conn.execute(sql1)
    conn.commit()
    conn.close()

def InsertData(aid):
    conn = sqlite3.connect('Data.db')
    postdata=vid.getinfo(aid)
    p=postdata['play']
    c=postdata['coins']
    ytrain=math.log(p,10)/(1+math.exp(2-50*c/p))
    if type(postdata)!=type(1):
        sql = '''insert into Data
                    (VIDEONUMBER,COMMENT,TID,PLAY,REVIEW,VIDEO_REVIEW,FAVORITES,MID,COINS,YTRAIN,TITLE,TYPENAME,DESCRIPTION)
                    values(%d,%d,%d,%d,%d,%d,%d,%d,%d,%.2f,'%s','%s','%s')''' % (aid,
                            postdata['comment'],
                            postdata['tid'],
                            postdata['play'],
                            postdata['review'],
                            postdata['video_review'],
                            postdata['favorites'],
                            postdata['mid'],
                            postdata['coins'],
                            ytrain,
                            postdata['title'],
                            postdata['typename'],
                            postdata['description'])
        conn.execute(sql)
        conn.commit()
        conn.close()

def ExportData(aid):
    conn = sqlite3.connect('Data.db')
    sql="SELECT * from Data where VIDEONUMBER=%d"%aid
    cur=conn.execute(sql)
    l1=cur.fetchall()
    l2=[]

    if len(l1):
        for i in range(0,9):
            l2.append(l1[0][i])
        l3=[l2[1:9], l1[0][9]]
        conn.close()
        return l3
    else:
        return 404


if __name__ ==  '__main__':
    pass
