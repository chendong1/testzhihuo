import requests

#获取登陆的token
def login_token():
        url='https://shuju.zhihuotech.com/api/login'
        header={
                'Host': 'shuju.zhihuotech.com',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
                'Origin': 'https://shuju.zhihuotech.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest':'empty',
                'Referer': "https://shuju.zhihuotech.com/login?redirect=%2Findex",
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
               # 'Cookie': 'rememberMe=true; username=chendong1; password=XIC1zsfYlxk0u03qxJ6+wCYy5JakWF2SdsdX0QX39g8I3gpbBhC4IcnhH1zhREov/4duwZ/U79gxvPXWtw5bRg=='
                  }
        params_form = {'username':'chendong1',
                       'password':'123456',
                       'code':'1111','uuid':'7ad5ee0aabca422b92ea12c1ed4ee0c9'}
        requests.packages.urllib3.disable_warnings()#去除警示提示
        r = requests.post(url=url,headers=header,params=params_form,verify=False)
        # print(r.url)#传递url参数
        # print(r.text)#想要内容
        # print(r.status_code)#状态码
        token = r.json()['token']
        return token


