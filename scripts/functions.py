# coding=utf-8
# @author: zenganiu
# @time: 2019/8/15 22:45

from scripts.mysql_connect import Rrjc_DB


# 文章列表展示
def Query(article):
	querys = Rrjc_DB()
	sql = 'select * from %s'%article
	data = querys.query(sql)
	querys.close()
	return data

# 文章详细页
def QueryArticle(article,id):
	querys = Rrjc_DB()
	sql = 'select * from %s where id=%s' %(article,id)
	data = querys.query(sql)
	print(data[0].get('authors'))
	if data[0].get('authors') == None:
		authors = ''
	else:
		authors = data[0].get('authors').split('"')[1]
	if data[0].get('tags') == None:
		tags = ''
	else:
		tags = data[0].get('tags').split('"')[1]
	print(authors,tags)
	querys.close()
	return data,authors,tags

# 文章翻译
def QueryTranslation(article,id):
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


def UpdataUser(id,handle):
	querys = Rrjc_DB()
	if handle == 'lockuser':
		sql = "update customer set is_active=0 where id=%s"%id
	if handle == 'unlockuser':
		sql = "update customer set is_active=1 where id=%s" % id
	if handle == 'deluser':
		sql = "delete from customer where id=%s" % id
	if handle == 'unlockuser':
		sql = "update customer set is_active=1 where id=%s" % id
	print(sql)
	data = querys.update(sql)
	querys.close()
	return data