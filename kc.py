'''
每日推送课表

'''
# -*- encoding:utf-8 -*-
import requests
import json
from urllib.parse import urlencode

from datetime import datetime



def num_to_char(num):
    """数字转中文"""
    num=str(num)
    new_str=""
    num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"日"}
    listnum=list(num)
    # print(listnum)
    shu=[]
    for i in listnum:
        # print(num_dict[i])
        shu.append(num_dict[i])
    new_str="".join(shu)
    # print(new_str)
    return new_str


pushtoken = '这里填pushplus的token'  # 这里填pushplus的token，可以在http://www.pushplus.plus/ 扫码注册

cj = {
    'token': pushtoken,
    'title': '课程推送',
    'content': '',
}

tsurl = 'http://www.pushplus.plus/send'
body = "{}"


try:
    def main(username,password):
        data = {'username': username, 'password': password, 'year': 2020, 'term': 12}
        dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
        url = "教务系统接口"
        res = requests.post(url, data)
        res = res.text
        res = json.loads(res)
        xinxi=[]
        if(res['success'] == True):
            for item in res['course']:
                # xinxi=[]
                if('星期'+num_to_char(dayOfWeek)==item['xqjmc']):
                    xinxi.append("课程名称："+item['kcmc']+" 地点："+item['cdmc']+" 节数："+item['jc']+" 星期："+item['xqjmc']+" 周数："+item['zcd'])
            grade=str(xinxi)
            cj['content'] = "今天课表如下:"+grade.replace('[','\n').replace(',','\n').replace(']','')
            print(grade)
            re = requests.post(url=tsurl, data=cj)
            print(re.text)
        else:
            cj['content'] = "成绩查询失败"
            re = requests.post(url=tsurl, data=cj)
            print(re.text)

    if __name__ == '__main__':
        main("学号xxxx", "xxxxx密码")

except:
    cj['content'] = '运行出错,请检查'
    re = requests.post(url=tsurl, data=cj)
    print(re.text)
