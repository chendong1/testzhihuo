import unittest

import pymysql
import requests


# pc按页扫描保存图片-生成exe_id


class TestShouJiPiGai(unittest.TestCase):
    # 准备url
    def setUp(self) :
        # 保存图片+生成exe_id的url
        self.url_user_get_list = "https://zhihuotech.com/mark_admin_dev/user/get_list"
        self.url_user_modify = "https://zhihuotech.com/mark_admin_dev/user/modify"
        print('开始执行用例')

    def tearDown(self) :
        print("用例结束")

    # 进入批改客服管理
    def test_user_get_list(self) :
        header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'zhihuotech.com',
            'Referer': 'https://zhihuotech.com/scan_web_dev_backup/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
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
        r = requests.post(url=self.url_user_get_list, json=form_data, headers=header)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')



    # 启用禁用按钮
    def test_user_modify(self) :

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

        params_data = {
            "correct_status": 0,
            "id": 609,
            "name": "string",
            "page_num": 0,
            "page_size": 0,
            "pass_status": 0,
            "position_type": 0,
            "subject_en": "string",
            "total": 0,
            "user_name": "string"
        }
        r = requests.post(url=self.url_user_modify, headers=header, json=params_data)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')


if __name__ == '__main__' :
    unittest.main()