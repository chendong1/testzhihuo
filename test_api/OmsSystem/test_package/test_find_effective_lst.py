import requests
# oms运营系统获取产品包权益有效期
url = "https://www.zhihuotech.com/oms_back_dev/oms/productPackageManager/find_effective_lst"
header = {
    'charset': 'utf-8',
    'content-type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Access-Control-Allow-Origin':'https://zhihuotech.com'
    }
parmes_date = { None }
r = requests.get(url=url,headers=header)
print(r.status_code)
print(r.url)
print(r.text)