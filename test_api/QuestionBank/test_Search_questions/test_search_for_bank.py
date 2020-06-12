import requests
import json
#按试题内容搜索
url='https://zhihuotech.com/bank/questionSearch/search_for_bank'
header={
    'Accept-Encoding': 'gzip' 'deflate' 'br',
    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '193',
    'Content-Type': 'application/json',
    'Host': 'zhihuotech.com',
    'Origin': 'https://zhihuotech.com',
    'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
form_data={
    'wd':'若一个三角形中有一个角是直角',
    'search_id':' ',
    'subject':'math',
    'types':[9],
    'chapters':[],
    'points':[],
    'page_num':1,
    'page_size':10,
    'filter_uuids':[],
    'ques_tags':[1]
}
r = requests.post(url=url,headers=header,json=form_data,verify=False)
print(r.url)
print(r.text)
print(r.status_code)