# coding=utf-8
# @Time    : 2019/8/13 15:03
# @Author  : zwa
import re,requests,json
import chardet
url = "http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh_CN&q=%s"%('Focus Antitrust')

r = requests.get(url)
print(type(r))
for i in r:
	print(i)
	print(type(i))
	str1 = i.decode()
	print(str1)
	data = json.loads(str1)
	print(type(data))


s = '\xe5\x85\xb3\xe6\xb3\xa8\xe5\x8f\x8d\xe6\x89\x98\xe6\x8b\x89\xe6\x96\xaf'

ss = s.encode('raw_unicode_escape')
print(ss)
sss = ss.decode()
print(sss)