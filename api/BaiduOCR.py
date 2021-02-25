# encoding:utf-8
import requests
import json
import base64

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

api_key = ""
secret_key = ""

ocr_map = {
    "汉语": "CHN_ENG",
    "英文": "ENG",
    "日语": "JAP",
    "韩语": "KOR",
    "法语": "FRE",
    "西班牙语": "SPA",
    "葡萄牙语": "POR",
    "德语": "GER",
    "意大利语": "ITA",
    "俄语": "RUS"
}


# def get_access_token(api_key, secret_key, re_generate=False):
#     if not re_generate:
#         # # 默认从文件中读取之前保存的token
#         # with open("./access_token.txt", "r") as f:
#         #     data = f.read()
#         #     if data == "":
#         #         return get_access_token(api_key, secret_key, re_generate=True)
#         #     return data
#         return "24.81b4b6b7c0c850fbbce1753edf5d0053.2592000.1616758434.282335-23700904"
#     else:
#         # client_id 为官网获取的AK， client_secret 为官网获取的SK
#         host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'
#         host = host.format(api_key, secret_key)
#         response = requests.get(host)
#         if response:
#             res = response.json()
#             access_token = res["access_token"]
#             # with open("./access_token.txt", "w") as f:
#             #     f.write(access_token)
#             return access_token
#         return None


# def get_ocr_result_from_file(img_path):
#     '''
#     通用文字识别, 图片从文件读取
#     '''
#     access_token = get_access_token(api_key, secret_key)
#     request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
#     # 二进制方式打开图片文件
#     f = open(img_path, 'rb')
#     img = base64.b64encode(f.read())
#     params = {
#         "image": img,
#         "language_type": "JAP"
#     }
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     if response:
#         return response.json()
#
#
# def get_ocr_result(img, type):
#     '''
#     通用文字识别， 直接传入图片base64编码后的字符串
#     '''
#     access_token = get_access_token(api_key, secret_key)
#     request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
#     params = {
#         "image": img,
#         "language_type": type
#     }
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     if response:
#         return response.json()

def get_ocr_result(img, type):
    url = "http://43.128.5.177:8080/OCR/getResult"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "imgBase64": str(img, encoding="utf-8"),
        "langType": type
    }
    body = json.dumps(body)
    r = requests.post(url=url, headers=headers, data=body)
    res = json.loads(r.text)
    return res


def get_ocr_result_from_file(img_path, type):
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())
    return get_ocr_result(img, type)
