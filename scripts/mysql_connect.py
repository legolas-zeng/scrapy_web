# coding=utf-8

import pymysql

class Rrjc_DB(object):
	def __init__(self):
		self.host = '127.0.0.1'
		self.port = '3306'
		self.passwd = 'qq1005521'
		self.user = 'root'
		self.db = 'article_source'
		self.cursor = self.conn()
	
	def conn(self):
		self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.db,
		                            charset="utf8",cursorclass=pymysql.cursors.DictCursor)
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