import requests
#根据uuid查询试题
uuid="3995423a-70cd-497e-80d7-a473fb8063f5"
url1 = "https://zhihuotech.com/bank/questionManage/getOneQuestionById/{}"
header = {'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODA1NjQxOSwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYjBjYjYzNGEtNmVkOS00NmU0LWI2MzEtZTgwM2FiYmY1YWMzIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.HRRtrwfM2HJ5yMVM2nthIW99tc3G4QbJ08HTSkmSDntfL8o-e1CT9lPsKxF4pAkVcUBn2Y_7b1vSKJhxQypB_mbyfKZyLUzLoK6Z9BKuRz0FdFNrwV_vDGgO6y7981ZCKBaCmpbyy7tuatfzU6EJvyPYUakqSBhncvXEA6R4pYw',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/json',
        'Host': 'zhihuotech.com',
        'Origin': 'https://zhihuotech.com',
        'Referer': 'https://zhihuotech.com/question_bank/add_question?go_show=2&username=wzg&uuid=3995423a-70cd-497e-80d7-a473fb8063f5&third_subject=english',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
r = requests.post(url=url1.format(uuid), headers=header, params=None,verify=False)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))
print(r.url)