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