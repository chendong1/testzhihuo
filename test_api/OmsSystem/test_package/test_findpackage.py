import requests
# oms运营系统请求产品包列表数据
url = "https://www.zhihuotech.com/oms_back_dev/oms/productPackageManager/findPackage"
header = {
    'charset': 'utf-8',
    'content-type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Access-Control-Allow-Origin':'https://zhihuotech.com'
    }
parmes_data = {'paqeNum':1,'pageSize':10}
r = requests.get(url=url,params=parmes_data,headers=header)
print(r.status_code)
print(r.url)
print(r.text)