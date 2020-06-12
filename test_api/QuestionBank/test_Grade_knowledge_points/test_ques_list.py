import requests
import json
#获取章节下的题
url='https://zhihuotech.com/bank/ques_bank/ques_list'
header = {
    'Accept-Encoding': 'gzip' 'deflate' 'br',
    'Accept-Language': 'zh-CN''zh''q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4NzYzMTI5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTYyYWE1NzktMDZiNC00NmViLWI4ZTUtMTBiMDE4Mjk5ODY3IiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.gyalkPb99QFkfqgXa2g_rx-Gx1Av_yNhhK5HVft97RGRvemKf-79G5yFvsXWQSN3Li2q6O8dnvE7mdc-_CefaDJvkEsoEycGnsZ2vVLMvpCMnxXYBczJ555D-X0GdoNcWOCkiw2zS3jg3UOswozeruKZmCFImYxt84DTNtEHKCs',
    'Connection': 'keep-alive',
    'Content-Length': '175',
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
form_data={"cate":21,
           "page_num":1,
           "page_size":10,
           "third_category_id":"af081e24-7496-451c-bb2e-475e991811f6",
           "subject":"chinese",
           "ques_tag":1,
           "user_id":1,
           "tag_flag":0,
           "point_id":"13725"
           }
r = requests.post(url=url,headers=header,json=form_data,verify=False)
print(r.url)
print(r.text)
print(r.status_code)