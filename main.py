'''
每日打卡自动执行并推送
'''
# -*- encoding:utf-8 -*-
import requests
import json
from urllib.parse import urlencode

pushtoken = ''  # 这里填pushplus的token，可以在http://www.pushplus.plus/ 扫码注册
jwsession = ''  # 这里填我在校园的jwsession

dk = {
    'token': pushtoken,
    'title': '我在校园每日打卡',
    'content': '',
}
header = {
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "2",
    "Host": "student.wozaixiaoyuan.com",
    "Accept-Language": "en-us,en",
    "Accept": "application/json, text/plain, */*",
    'JWSESSION':jwsession
}
dkurl = 'http://www.pushplus.plus/send'
body = "{}"

try:
    def main():
        url = "https://student.wozaixiaoyuan.com/health/save.json"
        sign_data = {
            "answers": '["0"]',
            "answer": '["0"]',
            "answer": '["0"]',
            # "seq": self.get_seq(),
            "temperature":"36.1",
            "temperature":"36.4",
            "temperature":"36.2",
            "latitude": "24.84835634567432",
            "longitude": "102.80318645678934",
            "country": "中国",
            "city": "昆明市",
            "district": "呈贡区",
            "province": "云南省",
            "township": "",
            "street": "",
        }
        data = urlencode(sign_data)
        response = requests.post(url=url, data=data, headers=header)
        response = json.loads(response.text)
        print(response)
        if response["code"] == 0:
            dk['content'] = "打卡成功"
            re = requests.post(url=dkurl, data=dk)
            print(re.text)
        else:
            dk['content'] = "打卡失败"
            re = requests.post(url=dkurl, data=dk)
            print(re.text)

    if __name__ == '__main__':
        main()

except:
    dk['content'] = '运行出错,请检查'
    re = requests.post(url=dkurl, data=dk)
    print(re.text)
