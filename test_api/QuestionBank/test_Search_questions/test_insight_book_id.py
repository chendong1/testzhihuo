import requests
import json
#获取教材id
url='https://zhihuotech.com/bank/knowledge_external_api/get_insight_book_by_id'
header={
    'Accept-Encoding': 'gzip'  'deflate'  'br',
    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODczNTk5MCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTRkMjRhODItYjQxMi00NDc0LThmMTEtZWU2NTYxM2RmMzZmIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.MEytqpo2i1m3G0qmmEJpdNjEGA-mFjzTTMxJFgcT2IL4-EA2kAzyrLNRQ_rau9YohOoAlPd1rC-puu2Lbjri6fH4R_CO6ZxFMlA7kgWfulz-8NpuOjAcpfpOuKLzdKbi1o_Kf9gZubFRKbZXXZCzCA7_JdQDIU4MvXhTFTt8A2A',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Host': 'zhihuotech.com',
    'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
Params_data={'insight_book_id': '624'}
r = requests.get(url=url,params=Params_data,headers=header,verify=False)
print(r.text)