import requests
import unittest
from test_api.DataSource.test_questiondate.test_login_token import login_token

class TestQesutionData(unittest.TestCase):
    def setUp(self):
        #智能练习数据分析和智能练习明细数据
        self.url_token = login_token()#获取登陆的token
        self.url_get_areas='https://zhihuotech.com/bank/question_area/get_areas'#获取地区
        self.url_search_condition = 'https://bi.zhihuotech.com/logtool-dev/logTool/insight_question/search_condition'#标签列表
        self.url_search_data='https://bi.zhihuotech.com/logtool-dev/logTool/insight_question/search_data'#题量计算
        print ('开始执行用例')

    def tearDown(self):
        print("用例结束")

    # 题量计算
    def test_get_search_data(self):
        header = {
            'Host': 'bi.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Bearer {}'.format(login_token()),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zhihuotech.com/question_bank/look_qnum?username=wzg&subject_en=math&edition_name=%E6%B2%AA%E7%A7%91%E6%96%B0%E7%89%88&book_name=%E5%88%9D%E4%B8%80%E4%B8%8A&subject_name=%E6%95%B0%E5%AD%A6&jump_insight_book_id=506&jump_bookid=b2cbc1f6-733a-4969-b657-f41c66f742f7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        form_data = {"book_id": "506", "chose_id_list": [], "custom_question_type": [], "page_num": 1, "page_size": 2,
                     "part_type": 0, "position_ids": [], "question_type": 1, "search_name": ""}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.post(url=self.url_search_data, headers=header, json=form_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 0, '获取地区失败')
        self.assertEqual(resuit['msg'], '成功', '获取地区失败')
        self.assertTrue('有理数' in r.text, '获取地区失败')#验证知识点

    # 标签列表
    def test_search_condition(self):
        header = {
            'Host': 'bi.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Bearer {}'.format(login_token()),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zhihuotech.com/question_bank/look_qnum?username=wzg&subject_en=math&edition_name=%E6%B2%AA%E7%A7%91%E6%96%B0%E7%89%88&book_name=%E5%88%9D%E4%B8%80%E4%B8%8A&subject_name=%E6%95%B0%E5%AD%A6&jump_insight_book_id=506&jump_bookid=b2cbc1f6-733a-4969-b657-f41c66f742f7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        params_data = {'bookId': '506'}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.get(url=self.url_search_condition, headers=header, params=params_data, verify=False)

        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 0, '标签列表失败')
        self.assertEqual(resuit['msg'], '成功', '标签列表失败')
        self.assertTrue('题目范围' in r.text, '标签列表失败')#验证题目

    # 获取地区
    def test_get_arear(self):
        header = {
            'Host': 'zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Bearer {}'.format(login_token()),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zhihuotech.com/question_bank/look_qnum?username=wzg&subject_en=math&edition_name=%E6%B2%AA%E7%A7%91%E6%96%B0%E7%89%88&book_name=%E5%88%9D%E4%B8%80%E4%B8%8A&subject_name=%E6%95%B0%E5%AD%A6&jump_insight_book_id=506&jump_bookid=b2cbc1f6-733a-4969-b657-f41c66f742f7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.get(url=self.url_get_areas, headers=header, params=None, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 0, '获取地区失败')
        self.assertEqual(resuit['msg'], '成功', '获取地区失败')
        self.assertTrue('全国通用' in r.text, '获取地区失败')#验证地区
if __name__=='__main__':
    unittest.main()