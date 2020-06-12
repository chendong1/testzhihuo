import unittest

import pymysql
import requests


# pc按页扫描保存图片-生成exe_id


class TestScanBackup(unittest.TestCase):
    # 准备url
    def setUp(self) :
        # 保存图片+生成exe_id的url
        self.url_save_per_page = "https://zhihuotech.com/mark_dev/paper/save_per_page"
        self.url_paper_result = "https://zhihuotech.com/mark_dev/paper/result"
        print('开始执行用例')

    def tearDown(self) :
        print("用例结束")

    # 保存图片
    def test_save_per_page(self) :
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
        r = requests.post(url=self.url_save_per_page, data=form_data, headers=header)
        result = r.json()
        print(r.json())

        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('null' in r.text, '数据不为空')  # 断言数据是否为空

    # 生成exe_id
    def test_paper_result(self) :
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

        params_data = {'exe_id' : get_status}
        r = requests.get(url=self.url_paper_result, headers=header, params=params_data)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('100.0' in r.text, '上传进度没有达到100%')  # 验证上传进度是否存在100%

if __name__ == '__main__' :
    unittest.main()
