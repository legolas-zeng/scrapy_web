# coding=utf-8
# @author: zenganiu
# @time: 2019/8/12 22:08

import xlwt,xlrd

# def HandleData(data,article):
# 	print(data)
# 	header = []
# 	for k in data:
# 		# print(data.get(k))
# 		header.append(k)
# 	filepath = creat_xls(header,article,data)
# 	return filepath
		
	
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
