import requests

# 老师查看批改报告预览-题目分析详情
url = "http://152.136.226.216:8198/report/teacher/detail"
header = {
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cache-Control' : 'no-cache',
    'Connection' : 'keep-alive',
    'content-type' : 'application/json',
    'Host' : 'zhihuotech.com',
    'Pragma' : 'no-cache',
    'Referer' : 'https://servicewechat.com/wx358a536fed195cc8/devtools/page-frame.html',
    'Sec-Fetch-Dest' : 'empty',
    'Sec-Fetch-Site' : 'cross-site',
    'Sec-Fetch-User' : '?F',
    'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'
}
params_data = {
    'batch_id' : '2020042903290704466',
    'class_id' : '31410007232205203',
    'tempalte_id' : '2',
    'question_ids' : '555866,555860,555877',
}
r = requests.get(url=url, headers=header, params=params_data)
print(r.json())
