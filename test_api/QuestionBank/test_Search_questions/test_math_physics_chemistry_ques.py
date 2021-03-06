import requests
import json
#获取数理化
url='https://zhihuotech.com/bank/ques_bank/math_physics_chemistry_ques'
header={
    'Accept-Encoding': 'gzip'  'deflate'  'br',
    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODczNTk5MCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTRkMjRhODItYjQxMi00NDc0LThmMTEtZWU2NTYxM2RmMzZmIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.MEytqpo2i1m3G0qmmEJpdNjEGA-mFjzTTMxJFgcT2IL4-EA2kAzyrLNRQ_rau9YohOoAlPd1rC-puu2Lbjri6fH4R_CO6ZxFMlA7kgWfulz-8NpuOjAcpfpOuKLzdKbi1o_Kf9gZubFRKbZXXZCzCA7_JdQDIU4MvXhTFTt8A2A',
    'Connection': 'keep-alive',
    'Content-Length': '325',
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
    'cate': '1',
    'page_num': '1',
    'page_size': '10',
    'point_no': 'e1',
    'subject': 'chemistry',
    'ques_tag': '4',
    'user_id': '1',
    'tag_flag': '0',
    'point_count_lst':[],
    'degree_lst':[],
    'point_behind': '0',
    'third_category_id': 'a66ccdf0-c610-46c3-919d-1ad9a7041155',
    'insight_book_id': '624',
    'question_type_list':[],
    'propositional_time_list':[],
    'point_id':'12460',
}
r = requests.post(url=url,headers=header,json=form_data,verify=False)
print(r.url)
print(r.text)
print(r.status_code)