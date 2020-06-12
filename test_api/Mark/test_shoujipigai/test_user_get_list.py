import requests

# bms 批改客服管理
url = "https://zhihuotech.com/mark_admin_dev/user/get_list"
header = {
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Connection' : 'keep-alive',
    'Host' : 'zhihuotech.com',
    'Referer' : 'https://zhihuotech.com/scan_web_dev_backup/',
    'Sec-Fetch-Dest' : 'empty',
    'Sec-Fetch-Mode' : 'cors',
    'Sec-Fetch-Site' : 'same-origin',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'X-Requested-With' : 'XMLHttpRequest'
}

form_data = {
  "correct_status": 0,
  "id": 0,
  "name": 'string',
  "page_num": 1,
  "page_size": 10,
  "pass_status": 0,
  "position_type": 0,
  "subject_en": "string",
  "total": 0,
  "user_name": "string"
}
r = requests.post(url=url, headers=header, json=form_data)
print(r.text)
print(r.json())
print(r.status_code)
