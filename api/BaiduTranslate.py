import requests
import json

"""
语言类型：
- CHN_ENG：中英文混合
- ENG：英文
- JAP：日语
- KOR：韩语
- FRE：法语
- SPA：西班牙语
- POR：葡萄牙语
- GER：德语
- ITA：意大利语
- RUS：俄语
"""


def get_translate_result(query_str, from_lang, to_lang):
    """
    获取翻译结果
    :param query_str: 要翻译的字符串
    :param from_lang: 源语言
    :param to_lang:  目标语言
    :return: 翻译后的字符串
    """
    url = "http://43.128.5.177:8080/translate/getResult"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "query": query_str,
        "from": from_lang,
        "to": to_lang
    }
    body = json.dumps(body)
    r = requests.post(url=url, headers=headers, data=body)
    res = json.loads(r.text)
    return res["trans_result"][0]["dst"]
