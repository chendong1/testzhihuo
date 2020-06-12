import requests
#获取相似试题，试题返回的地区
url = 'https://zhihuotech.com/bank/similarQuestion/listSimilarQuestion'
header = {'Accept': '*/*',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
          'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODkyMjE0NCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiNTVmMWQ4N2ItM2ZmOC00MDNhLThiMGEtNDBiODJmZTVlZTg5IiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.tKeI9T8DWb4O-y84UMu1OFfKAqapIRpzycjmT5lyoeqIX9aaSNsArKjePQoysUOc3h8g5IsujLMj7JkVJcPJnJEFlpqrlo6j72xsqpjs-804Cetlf0oJEq3YLaAobsggtY5ekwp_rds2Fu57fYFZR1ocpLRzfM-cOWR2RBwgT48',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive',
          'Content-Length': '321',
          'Content-Type': 'application/json',
          'Host': 'zhihuotech.com',
          'Origin': 'https://zhihuotech.com',
          'Pragma': 'no-cache',
          'Referer': 'https://zhihuotech.com/question_bank/same_question?pre_type=124&tiuuid=0c69e7bf-73b2-42c6-a630-61a871e4b488&subject=english&cate=125&ques_tag=1&similar_question_id=null',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-origin',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
          'X-Requested-With': 'XMLHttpRequest'}
form_data = {"cate":"2",
             "page_num":1,
             "question_uuid":"124e98de-3dd2-429e-87d0-0c97d3450377",
             "subject":"physics"}
r =  requests.post(url=url, headers=header,json=form_data,verify=False)
print(r)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))