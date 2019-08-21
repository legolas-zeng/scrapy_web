from typing import Text
import requests
import json


def split_content(content: str) -> list:
	"""将content根据5000长度进行分割组成数组list"""
	contenLen = len(content)
	limit = 5000
	nums = contenLen / limit
	content_list = []
	i = 0
	while i <= nums:
		start = i * limit
		end = start + limit
		if end < contenLen:
			content_list.append(content[start:end])
		else:
			content_list.append(content[start:])
			break
		i += 1
	return content_list


def google_response_clear(data: dict) -> str:
	"""清洗Google翻译返回的json数据，使其可以直接使用"""
	personArr = data.get("sentences")

	content = ''
	for i in range(len(personArr)):
		sentences = personArr[i]
		trans = sentences.get("trans")
		content += trans
	return content


def google_tranlation(content: str) -> str:
	url = "http://translate.google.cn/translate_a/single"
	params = {
		"client": "gtx", "dt": "t", "dj": "1", "ie": "UTF-8", "sl": "auto", "tl": "zh_CN",
		"q": content
	}
	resposne = requests.get(url=url, params=params)
	resposne.close()
	resposne_dict = resposne.json()
	content = google_response_clear(resposne_dict)
	return content


def translation_goole(content: str) -> str:
	# 将要翻译的内容content里换行符"\n"替换成空格
	content = content.replace('\n', '')

	# 将content根据5500长度进行分割组成数组list
	content_list = split_content(content)

	# 根据list里元素数去遍历翻译，返回一个list数组
	for i in range(len(content_list)):
		body = google_tranlation(content_list[i])
		content_list[i] = body

	# 将翻译后的list转换成字符串，作为返回参数
	text = ''.join(content_list)
	return text


def test_translation_goole():
	content = """
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
<p><em>İşçinin bir işyerinde
çalışmakta iken, mesai saatleri sonrasında ek
bir işte çalışıyor olması,
çalışma hakkı Anayasal bir hak
olduğundan mevcut işvereni tarafından
engellenemeyecektir, ancak iş ilişkisi kapsamında
sadakat yükümlülüğü ve rekabet
yasağı kriterlerine tabi tutulabilecektir.
İşçinin ek bir iş yapması, her somut
olay nezdinde değerlendirilmeli ve akabinde iş
sözleşmesinin işveren tarafından bu nedenle
feshinin söz konusu olup olamayacağına karar
verilmelidir. Yargıtay'ın özel dairelerinin,
işçinin ek iş yapması konusunda somut olay
nezdinde değerlendirme yapmış olduğu
kararları bulunmaktadır.</em></p>
	"""
	translation_goole(content)


if __name__ == "__main__":
	test_translation_goole()
