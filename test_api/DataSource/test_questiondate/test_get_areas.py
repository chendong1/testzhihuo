import requests
from test_api.DataSource.test_questiondate.test_login_token import login_token

#获取地区
url='https://zhihuotech.com/bank/question_area/get_areas'
header={
        'Host': 'zhihuotech.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': 'Bearer {}'.format(login_token()),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://zhihuotech.com/question_bank/look_qnum?username=wzg&subject_en=math&edition_name=%E6%B2%AA%E7%A7%91%E6%96%B0%E7%89%88&book_name=%E5%88%9D%E4%B8%80%E4%B8%8A&subject_name=%E6%95%B0%E5%AD%A6&jump_insight_book_id=506&jump_bookid=b2cbc1f6-733a-4969-b657-f41c66f742f7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
}
requests.packages.urllib3.disable_warnings()#去除警示提示
r = requests.get(url=url,headers=header,params=None,verify=False)
print(r.url)#传递url参数
print(r.text)#想要内容
print(r.status_code)#状态码