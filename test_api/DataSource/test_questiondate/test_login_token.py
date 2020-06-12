import requests

#获取登陆的token
def login_token():
    url = 'https://zhihuotech.com/auth_dev/oauth/token'
    header = {
        'Host': 'zhihuotech.com',
        'Connection': 'keep - alive',
        'Content-Length': '118',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Content-Type': 'application / json;charset = UTF - 8',
    'Accept': '*/*',
    'Origin': 'https://zhihuotech.com',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetc-Mode': 'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer': 'https://zhihuotech.com/question_bank/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh - CN, zh;q = 0.9'



    }
    form_date = {
        'username': 'wzg',
        'password': '123456',
        'grant_type': 'password',
        'client_id': 'insightClientId',
        'client_secret': 'insight',
    }
    requests.packages.urllib3.disable_warnings()  # 去除警示提示
    r = requests.post(url=url, headers=header, json=form_date, params=form_date,verify=False)
    # print(r.url)
    # print(r.text)
    # print(r.status_code)
    token = r.json()['access_token']
    return token



