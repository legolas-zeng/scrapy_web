# coding=utf-8

import pymysql

CENTERDB_INFO = {
	'host': 'localhost',
	'user': 'zwa',
	'pwd': 'qq1005521',
	'dbname': 'article_source',
	'port': 3306
}

class Rrjc_DB(object):
	def __init__(self):
		self.host = '192.168.3.5'
		self.port = '3306'
		self.passwd = 'qq1005521'
		self.user = 'zwa'
		self.db = 'article_source'
		self.cursor = self.conn()
	
	def conn(self):
		self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.db,
		                            charset="utf8")
		self.cor = self.conn.cursor()
		return self.cor
	
	def query(self, sql):
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	
	def insert_one(self, sql):
		result = self.cursor.execute(sql)
		self.conn.commit()
		return result
	
	# 插入多条数据
	def insert_many(self, sql, datas):
		result = self.cursor.executemany(sql, datas)
		self.conn.commit()
		return result
	
	# 更新数据
	def update(self, sql):
		result = self.cursor.execute(sql)
		self.conn.commit()
		return result
	
	# 关闭连接
	def close(self):
		self.cursor.close()
		self.conn.close()