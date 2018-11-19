import sqlite3
conn=sqlite3.connect('Data.db')
#创建数据表Data
sql1='''CREATE TABLE Data(
                VIDEONUMBER INTERGER    PRIMARY KEY     NOT NULL,
                COMMENT     INTERGER    NOT NULL,
                TID         INTERGER    NOT NULL,
                TYPENAME    TEXT        NOT NULL,
                PLAY        INTERGER    NOT NULL,
                REVIEW      INTERGER    NOT NULL,
                VIDEO_REVIEW    INTERGER    NOT NULL,
                FAVORITES   INTERGER    NOT NULL,
                TITLE       TEXT        NOT NULL,
                DESCRIPTION TEXT        NOT NULL,
                MID         INTERGER    NOT NULL,
                COINS       INTERGER    NOT NULL);'''

conn.execute(sql1)
conn.commit()
conn.close()