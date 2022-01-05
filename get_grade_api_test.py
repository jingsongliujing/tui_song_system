'''
每日推送成绩测试

'''
import requests
import json


def getScore(username, password):
    data = {
        'username': username,
        'password': password,
        'year': 2020,
        'term': 12
    }
    url = ""
    res = requests.post(url, data)
    res = res.text
    res = json.loads(res)
    a = []
    if (res['success'] == True):
        for item in res['grades']:
            print("课程名称：" + item['kcmc'] + " 成绩：" + item['cj'])
            a.append("课程名称：" + item['kcmc'] + " 成绩：" + item['cj'])
        print(a)
    else:
        print(res['message'])


getScore('账号', '密码')
