# coding=utf-8
# @Time    : 2019/8/13 15:03
# @Author  : zwa
import re,requests,json
import chardet
import xlwt
from newsweb.models import *
from scripts.mysql_connect import CDataBase

# idlist = ['1','2','3']
# for id in idlist:
# 	data = mondaq.objects.filter(id=id).values()
# 	print(data)
CENTERDB_INFO = {
        'host': 'localhost',
        'user': 'zwa',
        'pwd': 'qq1005521',
        'dbname': 'article_source',
        'port': 3306
    }

db_conn = CDataBase(CENTERDB_INFO['host'], CENTERDB_INFO['user'], CENTERDB_INFO['pwd'],
                                      CENTERDB_INFO['dbname'], CENTERDB_INFO['port'])
if db_conn._conn:
	a = db_conn.select_sql("select * from cnn")
	print(a)

# header = ['1','2','3']
# bdict = [['a','b','c'],['d','e','f']]
#
# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('data', cell_overwrite_ok=True)
#
# row = 1
# for k in bdict:
# 	j = 0
# 	for v in k:
# 		worksheet.write(row, j, v)
# 		j +=1
# 	row +=1
# i = 0
# for each_header in header:
# 	worksheet.write(0, i, each_header)  # 写入表头
# 	i += 1
#
# filepath = 'C:\\Users\Administrator\Desktop\\test.xls'
# workbook.save(filepath)