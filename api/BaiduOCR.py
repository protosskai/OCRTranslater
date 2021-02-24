# encoding:utf-8
import requests
import base64

api_key = ""
secret_key = ""


def get_access_token(api_key, secret_key, re_generate=False):
    if not re_generate:
        # 默认从文件中读取之前保存的token
        with open("./access_token.txt", "r") as f:
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
            with open("./access_token.txt", "w") as f:
                f.write(access_token)
            return access_token
        return None


def get_ocr_result(access_token, img_path):
    '''
    通用文字识别
    '''

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


if __name__ == '__main__':
    access_token = get_access_token(api_key, secret_key)
    res = get_ocr_result(access_token, "../1.png")
    print(res)
