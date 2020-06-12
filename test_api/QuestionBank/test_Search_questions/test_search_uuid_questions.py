import requests
import json
#使用uuid搜索试题
url='https://zhihuotech.com/bank/questionManage/getOneQuestionById/9a00628b-bbae-4e7d-8f09-17a5aa088265'
header={
    'Accept-Encoding': 'gzip' 'deflate' 'br',
    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '2',
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
}
r = requests.post(url=url,headers=header,json=form_data,verify=False)
print(r.url)
print(r.text)
print(r.status_code)