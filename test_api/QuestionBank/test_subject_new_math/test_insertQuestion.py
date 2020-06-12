import requests
#插入试题的录入时间
url = 'https://zhihuotech.com/bank/questionEntryStatistics/insertQuestion'
header = {'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '229',
        'Content-Type': 'application/json',
        'Host': 'zhihuotech.com',
        'Origin': 'https://zhihuotech.com',
        'Referer': 'https://zhihuotech.com/question_bank/physics_add?go_show=1&username=wzg&third_subject=math&subject_name=%E6%95%B0%E5%AD%A6',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
form_data = {"ques_uuid":"b8145216-90ab-46fa-a375-6cf2c3677fd5","subject":"math","user_name":"wzg","cate":2,"cate_name":"填空题","entry_time":442366,"start_time":"2020-04-23T05:34:59.735Z","end_time":"2020-04-23T05:42:22.101Z","type":"1"}
r =  requests.post(url=url, headers=header,json=form_data,verify=False)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))