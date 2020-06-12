import pymysql
import requests


# 扫描后生成exe_id
def correct_batch() :
    conn = pymysql.connect(host='bj-cdb-ihnudix4.sql.tencentcdb.com',
                           user='zhishi_qa',
                           database='mark_dev',
                           password='zhishiquan123$',
                           port=61704,
                           charset='utf8')

    cursor = conn.cursor()

    sql_select = "select * from correct_batch order by update_time desc limit 1 "

    cursor.execute(sql_select)
    result_one = cursor.fetchone()  # 选取一条结果
    get_status = result_one[0]
    print(get_status)
    cursor.close()
    conn.close()
    return get_status


get_exe_id = correct_batch()

url = "https://zhihuotech.com/mark_dev/paper/result"
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

params_data = {'exe_id' : get_exe_id}
r = requests.get(url=url, headers=header, params=params_data)
print(r.json())
print(r.status_code)
