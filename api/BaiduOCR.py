# encoding:utf-8
import requests
import base64

api_key = ""
secret_key = ""


def get_access_token(api_key, secret_key, re_generate=False):
    if not re_generate:
        # 默认从文件中读取之前保存的token
        with open("./api/access_token.txt", "r") as f:
            data = f.read()
            if data == "":
                return get_access_token(api_key, secret_key, re_generate=True)
            return data
    else:
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'
        host = host.format(api_key, secret_key)
        response = requests.get(host)
        if response:
            res = response.json()
            access_token = res["access_token"]
            with open("./api/access_token.txt", "w") as f:
                f.write(access_token)
            return access_token
        return None


def get_ocr_result_from_file(img_path):
    '''
    通用文字识别, 图片从文件读取
    '''
    access_token = get_access_token(api_key, secret_key)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())
    params = {
        "image": img,
        "language_type": "JAP"
    }
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()


def get_ocr_result(img):
    '''
    通用文字识别， 直接传入图片base64编码后的字符串
    '''
    access_token = get_access_token(api_key, secret_key)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    params = {
        "image": img,
        "language_type": "JAP"
    }
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()
