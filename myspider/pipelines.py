# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from os import path
from scrapy.xlib.pydispatch import dispatcher
import codecs
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
from myspider.items import MyspiderItem

class MyspiderPipeline(object):

	 # def __init__(self):
	 # 	self.file = codecs.open('test.json', 'w', encoding='utf-8')
	 # def process_item(self, item, spider):
	 # 		line = json.dumps(dict(item), ensure_ascii=False) + "\n" 
	 # 		self.file.write(line)
	 # 		return item 
	 # def spider_closed(self, spider): 
	 # 	self.file.close()


     # def __init__(self):
     # 	self.dbpool = adbapi.ConnectionPool('MySQLdb',db = 'test',user = 'root',passwd = 'root',cursorclass = MySQLdb.cursors.DictCursor,charset = 'utf-8',use_unicode = False)
     # def process_item(self, item, spider):
    	# query = self.dbpool.runInteraction(self._conditional_insert, item)

     # def _conditional_insert(self, tx, item):
    	# if item.get('title'):
    	# 	for i in range(len(item['title'])):
    	# 		tx.execute('insert into mydata values(%s,%s)',(item['title'][i],item['link'][i],item['company'][i],item['location'][i],item['gold'][i],item['online'][i]))



       

	 def __init__(self):
	 	self.conn = None

	 	dispatcher.connect(self.initialize,signals.engine_started)
	 	dispatcher.connect(self.finalize,signals.engine_stopped)

    def process_item(self, item, spider):
    	 self.conn.execute('insert into mytest values(?,?,?,?)',(None,'http://huizhou.58.com/zplvyoujiudian/24249901771835x.shtml'+item['link'][0],item['company'][0],item['title'][0],item['location'][0],item['gold'][0],item['online'][0]))

        return item
    def initialize(self):
    	if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            self.conn=self.create_table(self.filename)
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""create table mytest(id integer primary key autoincrement,link text,company text,title text,location text,gold text,online text)""")
        conn.commit()
        return conn

   
   

