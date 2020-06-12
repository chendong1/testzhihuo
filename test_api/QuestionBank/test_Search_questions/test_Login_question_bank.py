import requests
import json
#登录题库
url = 'https://zhihuotech.com/auth_dev/oauth/token'
header = {
    'Accept-Encoding': 'gzip' 'deflate' 'br',
    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODc1NzU0NCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiZjdlMjg3ODMtMWU3MC00NTQ5LWFiYmUtNzgyYTI1YTVjZjBmIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.Jhs2aZ1XBvktq-QNu2c78hj4HX2V4ApEUHnz9CnQNG_0NBxEkVZSY51mr-4Om7qJibD_Xxdz06rZ0mFw47goQEKvLlMTDwbxL-YMLDlyn3qs1KrQp7Zf9wewkpRIsenwZB4vPQBKCxZh7CHG1x-mBsChFpvoW2Z0UaVO0imSeWM',
    'Connection': 'keep-alive',
    'Content-Length': '118',
    'Content-Type': 'application/json' 'charset=UTF-8',
    'Host': 'zhihuotech.com',
    'Origin': 'https://zhihuotech.com',
    'Referer': 'https://zhihuotech.com/question_bank/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}
form_date = {
    'username': 'wzg',
    'password': '123456',
    'grant_type': 'password',
    'client_id': 'insightClientId',
    'client_secret':'insight',
 }
r = requests.post(url=url,headers=header,json=form_date,verify=False)
print(r.url)
print(r.text)
print(r.status_code)