import unittest
import requests

#查找知识点
class Testques_list(unittest.TestCase):
    def setUp(self):

        self.url_ques_list= 'https://zhihuotech.com/bank/ques_bank/ques_list'
        self.url_question_type= 'https://zhihuotech.com/bank/questionManage/get_question_type_by_subject'
        print('开始执行用例')
    def tearDown(self):
        print ('用例结束')

#获取章节下的题
    def test_ques_list(self):
        header = {
            'Accept-Encoding': 'gzip' 'deflate' 'br',
            'Accept-Language': 'zh-CN''zh''q=0.9',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4NzYzMTI5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTYyYWE1NzktMDZiNC00NmViLWI4ZTUtMTBiMDE4Mjk5ODY3IiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.gyalkPb99QFkfqgXa2g_rx-Gx1Av_yNhhK5HVft97RGRvemKf-79G5yFvsXWQSN3Li2q6O8dnvE7mdc-_CefaDJvkEsoEycGnsZ2vVLMvpCMnxXYBczJ555D-X0GdoNcWOCkiw2zS3jg3UOswozeruKZmCFImYxt84DTNtEHKCs',
            'Connection': 'keep-alive',
            'Content-Length': '175',
            'Content-Type': 'application/json',
            'Host': 'zhihuotech.com',
            'Origin': 'https://zhihuotech.com',
            'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        form_data = {"cate": 21,
                     "page_num": 1,
                     "page_size": 10,
                     "third_category_id": "af081e24-7496-451c-bb2e-475e991811f6",
                     "subject": "chinese",
                     "ques_tag": 1,
                     "user_id": 1,
                     "tag_flag": 0,
                     "point_id": "13725"
                     }
        r = requests.post(url=self.url_ques_list, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('chinese' in r.text)  #查看学科为语文

     #获取年级
    def test_question_type(self):
        header = {
        'Accept-Encoding': 'gzip' 'deflate' 'br',
        'Accept-Language': 'zh-CN''zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'zhihuotech.com',
        'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'subject': 'chinese',
    }
        params_data = {'subject': 'chinese'}
        r = requests.get(url=self.url_question_type, params=params_data, headers=header, verify=False)
        result=r.json()
        print(r.text)

        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')
        self.assertTrue('338' in r.text)#查看id是338

if __name__ == '__main__':
    unittest.main()