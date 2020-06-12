import requests
#专题组题：预览
url = 'https://zhihuotech.com/devj/applet/crate_examination/previewByTopic'
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
form_data = {"question_num_vos":[{"cate":"2","question_num":8,"question_count_num":24}],
             "class_id":"31410007232205170",
             "subject":"2",
             "create_union_id":"oyu3N0c42gIBsIUrayCFnV9JbpGo",
             "book_id":"46be896b-5a89-434b-bf45-26dc7ed43ecd",
             "category_ids":[""],
             "point_nos":[""],
             "point_ids":["54003"]}
r =  requests.post(url=url, headers=header,json=form_data,verify=False)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))