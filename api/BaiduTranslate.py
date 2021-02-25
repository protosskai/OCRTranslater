import requests
import json



translate_lang_map = {
    "汉语": "zh",
    "英文": "en",
    "日语": "jp",
    "韩语": "kor",
    "法语": "fra",
    "西班牙语": "spa",
    "葡萄牙语": "pt",
    "德语": "de",
    "意大利语": "it",
    "俄语": "ru"
}


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
