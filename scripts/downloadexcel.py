# coding=utf-8
# @author: zenganiu
# @time: 2019/8/12 22:08

import xlwt,xlrd
from newsweb.models import *
	
def HandleData(data,article):
	header = []
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet = workbook.add_sheet('data', cell_overwrite_ok=True)
	j = 0
	for k in data:
		header.append(k)
		worksheet.write(1, j, data.get(k))
		j +=1
	i = 0
	for each_header in header:
		worksheet.write(0, i, each_header)  # 写入表头
		i += 1
	filepath = 'C:\\Users\Administrator\Desktop\\%s.xls'%article
	workbook.save(filepath)
	return filepath

def MultHandleData(idlist,article):
	row = 1
	
	for id in idlist:
		print(id)
		if article == 'mondaq':
			data = mondaq.objects.filter(id=id).values()
		elif article == 'osac':
			data = osac.objects.filter(id=id).values()
		elif article == 'grada':
			data = grada.objects.filter(id=id).values()
		elif article == 'cnn':
			data = cnn.objects.filter(id=id).values()
		elif article == 'anvilgroup':
			data = anvilgroup.objects.filter(id=id).values()
		
		workbook = xlwt.Workbook(encoding='utf-8')
		worksheet = workbook.add_sheet('data', cell_overwrite_ok=True)
		j = 0
		header = []
		for k in data[0]:
			header.append(k)
			worksheet.write(row, j, data[0].get(k))
			j += 1
		print('第几行',row)
		row +=1
		i = 0
		print('333', header)
		for each_header in header:
			worksheet.write(0, i, each_header)  # 写入表头
			i += 1
	filepath = 'C:\\Users\Administrator\Desktop\\%s.xls' % article
	workbook.save(filepath)