'''
推送成绩

'''

# -*- encoding:utf-8 -*-
import requests
import json
from urllib.parse import urlencode

pushtoken = '这里填pushplus的token'  # 这里填pushplus的token，可以在http://www.pushplus.plus/ 扫码注册

cj = {
    'token': pushtoken,
    'title': '成绩推送',
    'content': '',
}

tsurl = 'http://www.pushplus.plus/send'
body = "{}"

try:

    def main(username, password):
        data = {
            'username': username,
            'password': password,
            'year': 2020,
            'term': 12
        }
        url = "教务系统接口"
        res = requests.post(url, data)
        res = res.text
        res = json.loads(res)
        xinxi = []
        if (res['success'] == True):
            for item in res['grades']:
                # xinxi=[]
                xinxi.append("课程名称：" + item['kcmc'] + " 成绩：" + item['cj'])
            grade = str(xinxi)
            cj['content'] = "成绩查询成功:" + grade.replace('[', '\n').replace(
                ',', '\n').replace(']', '')
            print(grade)
            re = requests.post(url=tsurl, data=cj)
            print(re.text)
        else:
            cj['content'] = "成绩查询失败"
            re = requests.post(url=tsurl, data=cj)
            print(re.text)

    if __name__ == '__main__':
        main('学号', '密码')

except:
    cj['content'] = '运行出错,请检查'
    re = requests.post(url=tsurl, data=cj)
    print(re.text)
