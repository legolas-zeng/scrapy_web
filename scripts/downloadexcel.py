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
	data_list = []
	for id in idlist:
		if article == 'mondaq':
			data = mondaq.objects.filter(id=id).values()
			data_list.append(data)
		elif article == 'osac':
			data = osac.objects.filter(id=id).values()
			data_list.append(data)
		elif article == 'grada':
			data = grada.objects.filter(id=id).values()
			data_list.append(data)
		elif article == 'cnn':
			data = cnn.objects.filter(id=id).values()
			data_list.append(data)
		elif article == 'anvilgroup':
			data = anvilgroup.objects.filter(id=id).values()
			data_list.append(data)
	filepath,filename = create_xls(data_list,article)
	
	return filepath,filename


def create_xls(data_list,article):
	print('文章类型',article)
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet = workbook.add_sheet('data', cell_overwrite_ok=True)
	
	row = 1
	header = []
	for data in data_list:
		j = 0
		for v in data[0]:
			# print('写入....',row, j,v)
			worksheet.write(0,j,v)
			worksheet.write(row, j, data[0].get(v))
			j += 1
		row +=1
	filepath = 'C:\\Users\Administrator\Desktop\\%s_%s.xls' %(article,len(data_list))
	filename = article + '_' + str(len(data_list))
	workbook.save(filepath)
	return filepath,filename
	
	# print('第几行',row)
	# row +=1
	# i = 0
	# print('333', header)
	# for each_header in header:
	# 	worksheet.write(0, i, each_header)  # 写入表头
	# 	i += 1
	# filepath = 'C:\\Users\Administrator\Desktop\\%s.xls' % article
	# workbook.save(filepath)