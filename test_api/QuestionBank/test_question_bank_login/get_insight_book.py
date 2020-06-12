import requests
#获取教材+年级接口列表
url=('https://zhihuotech.com/bank/knowledge_external_api/get_insight_book')
header = {'Content-Type': "application/json",
          'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3e''mciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU3NTk4NTk''1NSwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0x''FX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiZGJlNWZhYmQtYzNjYS0''0NDNiLTlmMzktN2JlNjFhZTc3MzY3IiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjox''fQ.w-1HS8KtPRpqnrjvu4z8UIvlBPqXm58TYQIht11F56G0gRrKFnlcXDb5LiGhManjkdwlTH0ytOihNKqku_''7-nccOIa8xAWr6Z9CJVXbAv6-a8aGUKSCKK3cKZbTnj0d94xWpuDRuOa2V3-KqdPVzhW3j3_8C-4S8Kvkgk4iKoDk',
          'Origin': 'https://zhihuotech.com',
          'Referer': 'https://zhihuotech.com/question_bank/'}
r = requests.get(url=url, headers=header,params=None,verify=False)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))