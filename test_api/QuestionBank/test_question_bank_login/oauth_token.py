import requests
import json
#登录题库
url=('https://zhihuotech.com/auth_dev/oauth/token')
general-header = {'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization':'null',
        'Connection':'keep-alive',
        'Content-Length':118,
        'Content-Type':'application/json;charset=UTF-8',
        'Host':'zhihuotech.com',
        'Origin':'https://zhihuotech.com',
        'Referer':'https://zhihuotech.com/question_bank/',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
data ={"username":"wzg","password":"123456","grant_type":"password","client_id":"insightClientId","client_secret":"insight"}
r = requests.post(url=url, data=data, headers=general-header,verify=False)
result = r.json()
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))