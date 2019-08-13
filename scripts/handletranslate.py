# coding=utf-8
# @Time    : 2019/8/13 13:56
# @Author  : zwa
from newsweb.models import *
from scripts import translater,translater2
# from GoogleFreeTrans import Translator
import re


def handledata(id,article:str):
	if article == 'mondaq':
		data = mondaq.objects.filter(id=id).values()
		tran_title, tran_content = Translated(data[0])
	elif article == 'osac':
		data = osac.objects.filter(id=id).values()
		tran_title,tran_content = Translated(data[0])
	elif article == 'grada':
		data = grada.objects.filter(id=id)
	elif article == 'cnn':
		data = cnn.objects.filter(id=id)
	elif article == 'anvilgroup':
		data = anvilgroup.objects.filter(id=id)
	return tran_title,tran_content

		
def Translated(data:dict):
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
	