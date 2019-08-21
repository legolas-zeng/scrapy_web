# coding=utf-8
# @author: zenganiu
# @time: 2019/8/15 22:45

from scripts.mysql_connect import Rrjc_DB
import re


# 文章列表展示
def Query(article):
	querys = Rrjc_DB()
	sql1 = 'select * from %s limit 1000' %article
	sql2 = 'select count(0) from %s' %article # 查询有多少条数据
	data1 = querys.query(sql1)
	data2 = querys.query(sql2)
	querys.close()
	return data1,data2

# 按页查询
def QueryPage(article,pagestart,pageend):
	querys = Rrjc_DB()
	sql1 = 'select * from %s limit %s,%s'%(article,pagestart,pageend)
	sql2 = 'select count(0) from %s' %article # 查询有多少条数据
	data1 = querys.query(sql1)
	data2 = querys.query(sql2)
	querys.close()
	return data1,data2

# 文章详细页
def QueryArticle(article,id):
	querys = Rrjc_DB()
	sql = 'select * from %s where id=%s' %(article,id)
	data = querys.query(sql)
	authors_list = []
	tags_list = []
	print('作者列表：',data[0].get('authors'))
	if data[0].get('authors') == None:
		authors_list = ''
	else:
		# authors = data[0].get('authors').split('"')[1]
		for j in range(len(data[0].get('authors').split('"'))):
			if j%2!=0:
				authors_list.append(data[0].get('authors').split('"')[j])
	if data[0].get('tags') == None:
		tags = ''
	else:
		# tags = data[0].get('tags').split('"')[1]
		for j in range(len(data[0].get('tags').split('"'))):
			if j % 2 != 0:
				tags_list.append(data[0].get('tags').split('"')[j])
	print(tags_list)
	querys.close()
	return data,authors_list,tags_list

# 获取一篇文章
# def QueryTranslation(article,id):
def QueryGetOneAriticle(article,id):
	querys = Rrjc_DB()
	sql = 'select * from %s where id=%s' % (article, id)
	data = querys.query(sql)
	querys.close()
	return data

# 文章搜索
def QuerySearch(article,title,startdate,enddate):
	querys = Rrjc_DB()
	titles = '%'+title+'%'
	sql = "select * from %s where title like '%s'and create_date >= '%s' and '%s'>= create_date " % (article, titles,startdate,enddate)
	print(sql)
	data = querys.query(sql)
	querys.close()
	return data

# 文章无标题搜索
def QuerySearchNoTitle(article,startdate,enddate):
	querys = Rrjc_DB()
	sql = "select * from %s where  create_date >= '%s' and '%s'>= create_date " % (article,startdate,enddate)
	print(sql)
	data = querys.query(sql)
	querys.close()
	return data

# 查询所有用户
def QueryUserList():
	querys = Rrjc_DB()
	sql = "select * from customer"
	data = querys.query(sql)
	querys.close()
	return data

# 查询VIP类型
def QueryVipType(name):
	querys = Rrjc_DB()
	sql = "select is_vip_type from customer where is_username='%s'"%name
	print(sql)
	data = querys.query(sql)
	querys.close()
	return data

# 更新用户信息
def UpdataUser(id,handle):
	querys = Rrjc_DB()
	if handle == 'lockuser':
		sql = "update customer set is_active=0 where id=%s"%id
	if handle == 'unlockuser':
		sql = "update customer set is_active=1 where id=%s" % id
	if handle == 'deluser':
		sql = "delete from customer where id=%s" % id
	# if handle == 'unlockuser':
	# 	sql = "update customer set is_active=1 where id=%s" % id
	print(sql)
	data = querys.update(sql)
	querys.close()
	return data

def AddUser(id,UserName,vip,staff,active):
	querys = Rrjc_DB()
	'''
	is_vip_type:
		默认为0，普通非vip用户
		管理员1，管理员的vip权限
		vip2，充值用户
	is_staff：
		默认0，false，非管理员
		1，ture，管理员
	is_active：
		默认1，ture，激活状态
		0，false，未激活
	is_superuser：
		默认0，false，非超级管理员
		1，ture，超级管理员
	'''
	if not vip:
		is_vip_type = 0
	else:
		is_vip_type = 2
	if not staff:
		is_staff = 0
	else:
		is_staff = 1
	if not active:
		is_active = 0
	else:
		is_active = 1
	sql = "INSERT INTO customer (`id`,`is_username`,`is_group`,`is_vip_type`,`is_staff`,`is_active`,`is_superuser`)VALUES('%s','%s','1','%s','%s','%s','0');"%(id,UserName,is_vip_type,is_staff,is_active)
	print(sql)
	data = querys.insert_one(sql)
	print(data)
	querys.close()