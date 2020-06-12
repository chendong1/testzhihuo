import requests
import json
#获取当前微信用户的班级列表
url='https://zhihuotech.com/devj/chk/is_new'
header={
    'charset': 'utf-8',
    'Accept-Encoding': 'gzip',
    'referer': 'https://servicewechat.com/wx358a536fed195cc8/0/page-frame.html',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MicroMessenger/7.0.9.1560(0x27000934) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
    'Host': 'zhihuotech.com',
    'Connection': 'Keep-Alive'
}
params_data={'union_id':'oyu3N0X-jvsSabhqSPhCQd42yZ-A'}
r = requests.get(url=url,params=params_data,headers=header,verify=False)
print(r.text)