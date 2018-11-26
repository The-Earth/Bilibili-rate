import sqlite3
import vid

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
    ytrain=1
    if type(postdata)!=type(1):
        sql = '''insert into Data
                    (VIDEONUMBER,COMMENT,TID,PLAY,REVIEW,VIDEO_REVIEW,FAVORITES,MID,COINS,YTRAIN,TITLE,TYPENAME,DESCRIPTION)
                    values(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s','%s')''' % (aid,
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
    l=cur.fetchall()
    conn.close()
    return l

if __name__ ==  '__main__':
    pass
