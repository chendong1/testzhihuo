import requests

# 扫描保存图片接口
url = "https://zhihuotech.com/mark_dev/paper/save_per_page"
header = {
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Connection' : 'keep-alive',
    'Content-Length' : '0',
    'Host' : 'zhihuotech.com',
    'Origin' : 'https://zhihuotech.com',
    'Referer' : 'https://zhihuotech.com/scan_web_dev_backup/',
    'Sec-Fetch-Dest' : 'empty',
    'Sec-Fetch-Mode' : 'cors',
    'Sec-Fetch-Site' : 'same-origin',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'X-Requested-With' : 'XMLHttpRequest'
}
form_data = {
    'exe_id' : '36633',
    'page_url' : 'https://images-dev-1256880427.cos.ap-beijing.myqcloud.com/insightPaper/36633_1587464651509test_11.jpg',
    'page_num' : '11'
}
r = requests.post(url=url, data=form_data, headers=header)
print(r.text)
print(r.json())
print(r.status_code)
