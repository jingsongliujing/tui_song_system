'''
每日推送课表测试
'''
import requests
import json
from datetime import datetime


def num_to_char(num):
    """数字转中文"""
    num = str(num)
    new_str = ""
    num_dict = {
        "0": u"零",
        "1": u"一",
        "2": u"二",
        "3": u"三",
        "4": u"四",
        "5": u"五",
        "6": u"六",
        "7": u"日"
    }
    listnum = list(num)
    # print(listnum)
    shu = []
    for i in listnum:
        # print(num_dict[i])
        shu.append(num_dict[i])
    new_str = "".join(shu)
    # print(new_str)
    return new_str


def getScore(username, password):
    dayOfWeek = datetime.now().isoweekday()  ###返回数字1-7代表周一到周日
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
    if (res['success'] == True):
        for item in res['course']:
            if ('星期' + num_to_char(dayOfWeek) == item['xqjmc']):
                # if('星期'+num_to_char(1)==item['xqjmc']):
                print("课程名称：" + item['kcmc'] + " 地点：" + item['cdmc'] + " 节数：" +
                      item['jc'] + " 星期：" + item['xqjmc'] + " 周数：" +
                      item['zcd'])
    else:
        print(res['message'])


getScore("学号", "密码")