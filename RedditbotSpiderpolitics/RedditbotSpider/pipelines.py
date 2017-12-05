# -*- coding: utf-8 -*-

#Scrapy pipeline to SQLite3 database borrowed & modified:
#https://github.com/sunshineatnoon/Scrapy-Amazon-Sqlite/blob/master/amazon/pipelines.py

import sqlite3
import os
con = None

class RedditscrapyPipeline(object):
    
    def __init__(self):
        self.setupDBCon()
        self.createTables()
        
    def setupDBCon(self):
        self.con = sqlite3.connect(os.getcwd() + '/test.db')
        self.cur = self.con.cursor()
    
    def createTables(self):
        self.dropsenTable()
        self.createsenTable()
    
    def dropsenTable(self):
        self.cur.execute("DROP TABLE IF EXISTS sen")
    
    def closeDB(self):
        self.con.close()
        
    def __del__(self):
        self.closeDB()
        
    def createsenTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS sen(id INTEGER PRIMARY KEY NOT NULL, \
            title TEXT, \
            comments TEXT \
            )")   
    
    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self,item):
        self.cur.execute("INSERT INTO sen(\
            title, \
            comments \
            ) \
        VALUES( ?, ?)", \
        ( \
            str(item.get('title','')),
            str(item.get('comments',''))
        ))
        self.con.commit()                    
