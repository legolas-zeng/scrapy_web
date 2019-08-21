import requests
import uuid
import random
import hashlib


class Translation:
    def __init__(self, content):
        # 初始化：清理掉空格，并将content进行切割
        # self.content = content.replace('\n', '')
        self.content = content
        self.limit = 4500  # 切割长度
        self.content_list = []
        self.content_list_translation = []
        self.result = ''  # 翻译结果

    def __split_content(self, limit=5000):
        """将content根据limit长度进行分割组成数组list"""
        self.content_list = []
        contenLen = len(self.content)
        nums = contenLen / limit
        i = 0
        while i <= nums:
            start = i * limit
            end = start + limit
            if end < contenLen:
                self.content_list.append(self.content[start:end])
            else:
                self.content_list.append(self.content[start:])
                break
            i += 1

    def google_response_clear(self, data: dict):
        """清洗Google翻译返回的json数据，使其可以直接使用"""
        personArr = data.get("sentences")

        content = ''
        for i in range(len(personArr)):
            sentences = personArr[i]
            trans = sentences.get("trans")
            content += trans
        return content

    def google_api(self, content):
        """进行google翻译API"""
        url = "http://translate.google.cn/translate_a/single"
        params = {
            "client": "gtx", "dt": "t", "dj": "1", "ie": "UTF-8", "sl": "auto", "tl": "zh_CN",
            "q": content
        }
        response = requests.get(url=url, params=params)
        response.close()
        if response.status_code != 200:
            # 429是访问次数太多Google限制访问
            text = '请求Google翻译接口太多了，被限制一段时间不能访问了！！！'
            print('=' * 10, text, '=' * 10)
            return False, text
        resposne_dict = response.json()
        content = self.google_response_clear(resposne_dict)
        return True, content

    def goole_translation_free(self):
        """ Google翻译接口
        :return: 成功：返回翻译的内容; 失败：False
        """
        # 切割content
        self.__split_content()

        # 根据list里元素数去遍历翻译，返回一个list数组
        print('=' * 10, '使用Google免费翻译接口', '=' * 10)
        self.content_list_translation = []  # 清空
        for i in range(len(self.content_list)):
            _bool, body = self.google_api(self.content_list[i])
            if not _bool:
                # Google限制访问
                return False, body
            self.content_list_translation.append(body)

        # 将翻译后的list转换成字符串，作为返回参数
        self.result = ''.join(self.content_list_translation)
        return True, self.result

    def youdao_response_clear(self, data: dict):
        """清洗有道翻译返回的dict数据，使其可以直接使用"""
        # personArr = data.get("translateResult")[0]
        personArr = data.get("translateResult")

        content = ''
        for i in range(len(personArr)):
            translateResult = personArr[i]
            # trans = translateResult.get("tgt")
            trans = translateResult[0].get("tgt")
            content += trans
        return content

    def youdao_api(self, content):
        """进行有道翻译API：该API无法自动识别HTML标签"""
        url = "http://fanyi.youdao.com/translate"
        params = {
            "doctype": "json", "type": "auto", "i": content
        }

        response = requests.get(url=url, params=params)
        response.close()
        if response.status_code != 200:
            text = response.text
            print('ERROR: ', text)
            return False, text
        resposne_dict = response.json()
        content = self.youdao_response_clear(resposne_dict)
        return True, content

    def youdao_translation_free(self):
        """ 有道翻译接口：不建议使用，翻译效果太差
        :return: 成功：返回翻译的内容; 失败：False
        """
        # 切割content
        self.__split_content()

        # 根据list里元素数去遍历翻译，返回一个list数组
        print('=' * 10, '使用有道免费翻译接口', '=' * 10)
        self.content_list_translation = []  # 清空
        for i in range(len(self.content_list)):
            _bool, body = self.youdao_api(self.content_list[i])
            if not _bool:
                # Google限制访问
                return False, '接口报错'
            # self.content_list[i] = body
            self.content_list_translation.append(body)

        # 将翻译后的list转换成字符串，作为返回参数
        self.result = ''.join(self.content_list_translation)
        return True, self.result

    def biying_response_clear(self, data: dict):
        """清洗必应翻译返回的dict数据，使其可以直接使用"""
        content = data[0]['translations'][0]['text']
        return content

    def biying_api(self, content):
        """进行必应翻译API：该API无法自动识别HTML标签"""
        subscriptionKey = '41cf969bbe004508917b410af36f97f0'  # 必应秘钥
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'
        params = '&to=zh-Hans'
        url = base_url + path + params
        headers = {
            'Ocp-Apim-Subscription-Key': subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': content
        }]

        response = requests.post(url=url, headers=headers, json=body)
        response.close()
        if response.status_code != 200:
            text = response.text
            print('ERROR: ', text)
            return False, text
        resposne_dict = response.json()
        content = self.biying_response_clear(resposne_dict)
        return True, content

    def biying_translation(self):
        """ 必应翻译接口：不支持带HTML标签翻译，要用文本content_text
        :return: 成功：返回翻译的内容; 失败：False
        """
        # 切割content
        self.__split_content(limit=4500)

        # 根据list里元素数去遍历翻译，返回一个list数组
        print('=' * 10, '使用必应翻译接口(每月免费200万字符)', '=' * 10)
        self.content_list_translation = []  # 清空
        for i in range(len(self.content_list)):
            _bool, body = self.biying_api(self.content_list[i])
            if not _bool:
                return False, body
            self.content_list_translation.append(body)

        # 将翻译后的list转换成字符串，作为返回参数
        self.result = ''.join(self.content_list_translation)
        return True, self.result

    def baidu_response_clear(self, data: dict):
        """清洗百度翻译返回的dict数据，使其可以直接使用"""
        personArr = data.get("trans_result")

        content = ''
        for i in range(len(personArr)):
            translateResult = personArr[i]
            trans = translateResult.get("dst")
            content += trans
        return content

    def baidu_api(self, content):
        """进行百度翻译API：支持HTML标签翻译"""
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        appid = '20190820000327976'
        secretKey = 'T6QdWM6t6aURndMhH63w'
        salt = random.randint(32768, 65536)

        sign = appid + content + str(salt) + secretKey
        m = hashlib.md5()
        m.update(sign.encode('utf-8'))
        sign = m.hexdigest()

        params = {
            'appid': appid,
            'from': 'auto',
            'to': 'zh',
            'salt': salt,
            'sign': sign,
            'q': content
        }
        response = requests.get(url=url, params=params)
        response.close()
        if 'error_code' in response.text or response.status_code != 200:
            text = response.text
            print('ERROR: ', text)
            return False, text
        resposne_dict = response.json()
        content = self.baidu_response_clear(resposne_dict)
        return True, content

    def baidu_translation(self):
        """ 百度翻译接口：支持带HTML标签翻译
        :return: 成功：返回翻译的内容; 失败：False
        """
        # 切割content
        self.__split_content(limit=4000)

        # 根据list里元素数去遍历翻译，返回一个list数组
        print('=' * 10, '使用百度翻译接口(每月免费200万字符)', '=' * 10)
        self.content_list_translation = []  # 清空
        for i in range(len(self.content_list)):
            _bool, body = self.baidu_api(self.content_list[i])
            if not _bool:
                return False, body
            self.content_list_translation.append(body)

        # 将翻译后的list转换成字符串，作为返回参数
        self.result = ''.join(self.content_list_translation)
        return True, self.result

def test_translation():
    content1 = """
    	        <div id="articlebody"><p><em>First published in The Royal Gazette, Legally Speaking, July
    	2019</em></p>
    	<p>In the ever-changing world of politics and their related global
    	financial sanctions, it is imperative that businesses understand
    	the financial sanctions regimes in place and have effective methods
    	to screen their systems for any potential breaches.</p>
    	<p>The dynamic nature of the global sanctions landscape is vividly
    	illustrated when one considers Brexit, where the United Kingdom may
    	be required to introduce an entirely new and independent sanctions
    	regime once it has exited the European Union; or the United States,
    	where there is increasing focus on secondary sanctions.</p>
    	<p>Financial sanctions are imposed to combat money laundering,
    	terrorist financing and the development of weapons of mass
    	destruction. Sanctions are primarily imposed by the United Nations,
    	EU, US and UK. Such measures range from comprehensive economic and
    	trade sanctions to more targeted measures such as arms embargoes,
    	travel bans, financial or diplomatic restrictions.</p>
    	<p>As each country's sanctions tend to be applicable to
    	citizens of that country, and bodies formed or incorporated under
    	the laws of that country, it is important to understand any
    	obligations that follow from having links to another country.</p>
    	<p>Bermuda enforces the same financial sanctions imposed in the UK.
    	Sanctions are generally brought into force under the International
    	Sanctions Act 2003. The International Sanctions Regulations 2013
    	set out all the regime-related sanctions orders in force in Bermuda
    	and are referred to as the Bermuda International Sanctions Regime.
    	All individuals and legal entities who are within or undertake
    	activities within Bermuda must comply.</p>
    	<p>It can be challenging to comply with multi-jurisdictional
    	restrictions due to the frequency with which they change. It is
    	therefore critical that businesses understand which regimes their
    	entity must observe in addition to the sanctions imposed under
    	Bermuda law. Merely dealing in a jurisdiction's currency can
    	bring a business within the scope of that jurisdiction's
    	regime.</p>
    	<p>Companies must review and test their sanctions screening system
    	to ensure effectiveness, efficiency and responsiveness to the
    	ever-changing sanctions regimes. It is a criminal offence to breach
    	the obligations under the respective sanctions. Penalties for
    	failure to comply vary but, upon conviction, they can include
    	imprisonment and/or a fine. In addition to criminal penalties, non-
    	compliance by an entity licensed by the Bermuda Monetary Authority
    	can lead to regulatory action including cancellation of
    	registration, public censure and a civil fine of up to $10
    	million.</p>
    	<p>Consequently, companies must identify and assess the relevant
    	sanctions risks it may be exposed to, whether in respect of certain
    	regimes or entities, and implement a sanctions screening programme
    	proportionate with the company's nature, size and
    	complexity.</p>
    	<p>To be effective, consideration should be given to matters such
    	as the company's location and its proximity to sanctioned
    	companies; the location of its customers; the volume of
    	transactions and distribution channels; and whether the types of
    	products and services offered represent a heightened sanctions
    	risk, for example, foreign correspondent accounts, cross-border
    	transactions, or trade-related products.</p>
    	<p>Two screening measures are commonly implemented, customer
    	screening and transaction screening. Customer screening is intended
    	to identify sanctioned individuals or entities during the
    	on-boarding process and the lifespan of the customer relationship,
    	while transaction screening is used to identify transactions
    	involving sanctioned individuals or entities.</p>
    	<p>Together, customer and transaction screening that account for
    	the relevant business specific matters previously mentioned can
    	create a powerful system of controls that will identify targets of
    	sanctions.</p>
    	<p>Notwithstanding this, screening alone is not sufficient to
    	ensure complete compliance with obligations imposed under financial
    	sanctions. Screening must be implemented alongside other financial
    	crime risk prevention processes and as part of a wider compliance
    	programme.</p>
    	<p><em>The content of this article is intended to provide a general
    	guide to the subject matter. Specialist advice should be sought
    	about your specific circumstances.</em></p>
    	</div>
    	    """
    content1_text = """
    	        First published in The Royal Gazette, Legally Speaking, July
    	2019
    	 In the ever-changing world of politics and their related global
    	financial sanctions, it is imperative that businesses understand
    	the financial sanctions regimes in place and have effective methods
    	to screen their systems for any potential breaches.
    	 The dynamic nature of the global sanctions landscape is vividly
    	illustrated when one considers Brexit, where the United Kingdom may
    	be required to introduce an entirely new and independent sanctions
    	regime once it has exited the European Union; or the United States,
    	where there is increasing focus on secondary sanctions.
    	 Financial sanctions are imposed to combat money laundering,
    	terrorist financing and the development of weapons of mass
    	destruction. Sanctions are primarily imposed by the United Nations,
    	EU, US and UK. Such measures range from comprehensive economic and
    	trade sanctions to more targeted measures such as arms embargoes,
    	travel bans, financial or diplomatic restrictions.
    	 As each country's sanctions tend to be applicable to
    	citizens of that country, and bodies formed or incorporated under
    	the laws of that country, it is important to understand any
    	obligations that follow from having links to another country.
    	 Bermuda enforces the same financial sanctions imposed in the UK.
    	Sanctions are generally brought into force under the International
    	Sanctions Act 2003. The International Sanctions Regulations 2013
    	set out all the regime-related sanctions orders in force in Bermuda
    	and are referred to as the Bermuda International Sanctions Regime.
    	All individuals and legal entities who are within or undertake
    	activities within Bermuda must comply.
    	 It can be challenging to comply with multi-jurisdictional
    	restrictions due to the frequency with which they change. It is
    	therefore critical that businesses understand which regimes their
    	entity must observe in addition to the sanctions imposed under
    	Bermuda law. Merely dealing in a jurisdiction's currency can
    	bring a business within the scope of that jurisdiction's
    	regime.
    	 Companies must review and test their sanctions screening system
    	to ensure effectiveness, efficiency and responsiveness to the
    	ever-changing sanctions regimes. It is a criminal offence to breach
    	the obligations under the respective sanctions. Penalties for
    	failure to comply vary but, upon conviction, they can include
    	imprisonment and/or a fine. In addition to criminal penalties, non-
    	compliance by an entity licensed by the Bermuda Monetary Authority
    	can lead to regulatory action including cancellation of
    	registration, public censure and a civil fine of up to $10
    	million.
    	 Consequently, companies must identify and assess the relevant
    	sanctions risks it may be exposed to, whether in respect of certain
    	regimes or entities, and implement a sanctions screening programme
    	proportionate with the company's nature, size and
    	complexity.
    	 To be effective, consideration should be given to matters such
    	as the company's location and its proximity to sanctioned
    	companies; the location of its customers; the volume of
    	transactions and distribution channels; and whether the types of
    	products and services offered represent a heightened sanctions
    	risk, for example, foreign correspondent accounts, cross-border
    	transactions, or trade-related products.
    	 Two screening measures are commonly implemented, customer
    	screening and transaction screening. Customer screening is intended
    	to identify sanctioned individuals or entities during the
    	on-boarding process and the lifespan of the customer relationship,
    	while transaction screening is used to identify transactions
    	involving sanctioned individuals or entities.
    	 Together, customer and transaction screening that account for
    	the relevant business specific matters previously mentioned can
    	create a powerful system of controls that will identify targets of
    	sanctions.
    	 Notwithstanding this, screening alone is not sufficient to
    	ensure complete compliance with obligations imposed under financial
    	sanctions. Screening must be implemented alongside other financial
    	crime risk prevention processes and as part of a wider compliance
    	programme.
    	 The content of this article is intended to provide a general
    	guide to the subject matter. Specialist advice should be sought
    	about your specific circumstances.
    	    """
	
    trans = Translation(content1)
    _bool, content = trans.goole_translation_free()
    print(content)
    _bool, content = trans.youdao_translation_free()
    print(content)
    _bool, content = trans.biying_translation()
    print(content)
    _bool, content = trans.baidu_translation()
    print(content)

if __name__ == "__main__":
    test_translation()