# coding=utf-8
# @Time    : 2019/8/13 13:56
# @Author  : zwa
from newsweb.models import *
from scripts import translater,translater2,functions,translation
# from GoogleFreeTrans import Translator
import re



def handledata(id,article:str):
	data = functions.QueryGetOneAriticle(article, id)
	tran_title, tran_content = Translated(data[0])
	# if article == 'mondaq':
	# 	data = mondaq.objects.filter(id=id).values()
	# 	tran_title, tran_content = Translated(data[0])
	if data[0].get('authors') == None:
		authors = ''
	else:
		authors = data[0].get('authors').split('"')[1]
	if data[0].get('tags') == None:
		tags = ''
	else:
		tags = data[0].get('tags').split('"')[1]
	article_time = data[0].get('create_date')
	return tran_title,tran_content,authors, tags,article_time

		
def Translated(data):
	title = data.get("title")
	content = data.get('content')
	# print(content)
	tran_title = translater.translate(title)
	tran_content_list = ''
	if len(content) > 4000:
		req_content = cut_text(content)
		for i in req_content:
			print('++++',len(i))
			tran_content = translater.translate(i)
			# print(tran_content)
			tran_content_list = tran_content_list+tran_content
	else:
		tran_content_list = translater.translate(content)
	
	return tran_title,tran_content_list

def cut_text(text,lenth=4000) -> list:
	retext = text.replace('\n', ' ')
	textArr = re.findall('.{' + str(lenth) + '}', retext)
	textArr.append(text[(len(textArr) * lenth):])
	return textArr

def HandleData(id,article):
	data = functions.QueryGetOneAriticle(article, id)
	trans1 = translation.Translation(data[0].get('content'))
	_bool1, content1 = trans1.goole_translation_free()
	trans2 = translation.Translation(data[0].get('title'))
	_bool2, content2 = trans2.goole_translation_free()
	if _bool1 and _bool2:
		return content1, content2