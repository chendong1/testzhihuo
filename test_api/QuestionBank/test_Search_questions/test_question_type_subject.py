import requests
import json
#获取科目和题型
url='https://zhihuotech.com/bank/questionManage/get_question_type_by_subject'
header={
    'Accept-Encoding': 'gzip'  'deflate'  'br',
    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
    'Connection': 'keep-alive',
    'Host': 'zhihuotech.com',
    'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
Params_data={'subject': 'chemistry'}
r = requests.get(url=url,params=Params_data,headers=header,verify=False)
print(r.text)