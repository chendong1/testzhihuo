import requests
#获取专题树
url = 'https://zhihuotech.com/bank/thematic_tree/get_thematic_point'
header = {'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
         'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
         'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'zhihuotech.com',
        'Referer': 'https://zhihuotech.com/question_bank/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
params_data = {'subject':'chinese'}
r = requests.get(url=url, headers=header,params=params_data,verify=False)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))