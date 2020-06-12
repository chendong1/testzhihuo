import json
import unittest
import requests
class TestSubject_new_math(unittest.TestCase):
    #新增数学填空题及相关接口调用
    def setUp(self):
        self.url_get_visible_book = 'https://zhihuotech.com/bank/book_manager/get_visible_book'
        #self.url_get_insight_point_no_deleted_by_subject = 'https://zhihuotech.com/insight_dev/pointTreeManager/get_insight_point_no_deleted_by_subject'
        self.url_get_insight_third_subject = 'https://zhihuotech.com/bank/questionManage/get_insight_third_subject'
        self.url_get_all_projects = 'https://zhihuotech.com/bank/questionManage/get_all_projects'
        self.url_get_insight_question_type_type_pre_by_subject ='https://zhihuotech.com/bank/questionManage/get_insight_question_type_type_pre_by_subject'
        self.url_listTopicBySubjectEn="https://zhihuotech.com/bank/questionManage/listTopicBySubjectEn/{}"
        self.url_get_insight_book = 'https://zhihuotech.com/bank/knowledge_external_api/get_insight_book'
        self.url_get_point_by_book_type='https://zhihuotech.com/bank/pointTreeNoEnglishController/get_point_by_book_type'
        self.url_get_insight_book_by_id = 'https://zhihuotech.com/bank/knowledge_external_api/get_insight_book_by_id'
        self.url_get_question_type_by_subject = 'https://zhihuotech.com/bank/questionManage/get_question_type_by_subject'
        self.url_get_insight_question_type_type_by_subject = 'https://zhihuotech.com/bank/questionManage/get_insight_question_type_type_by_subject'
        self.url_get_projects_by_point_ids = 'https://zhihuotech.com/bank/questionManage/get_projects_by_point_ids'
        self.url_get_methods_by_point_ids = 'https://zhihuotech.com/bank/questionManage/get_methods_by_point_ids'
        self.url_submit_question = 'https://zhihuotech.com/bank/questionManage/submit_question'
        self.url_insertQuestion="https://zhihuotech.com/bank/questionEntryStatistics/insertQuestion"
    print('开始执行用例')
    # 根据学科获取知识点列表

    def test_get_visible_book(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math'}
        r = requests.get(url=self.url_get_visible_book, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('苏科版' in r.text)  # 验证教材版本包含苏科版

    '''def test_get_insight_point_no_deleted_by_subject(self):
        headers = {'Accept': '*/*',
                           'Accept-Encoding': 'gzip, deflate, br',
                           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                           'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                           'Connection': 'keep-alive',
                           'Content-Type': 'application/json',
                           'Host': 'zhihuotech.com',
                           'Referer': 'https://zhihuotech.com/question_bank/',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'same-origin',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                           'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math'}
        r = requests.get(url=self.url_get_insight_point_no_deleted_by_subject, headers=headers, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('函数' in r.text) #获取题型'''

    # 获取学科列表
    def test_get_insight_third_subject(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'pointId': 46113}
        r = requests.get(url=self.url_get_insight_third_subject, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('初中数学' in r.text)  # 获取教材初中数学

    # 查询所有的专题
    def test_get_all_projects(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math'}
        r = requests.get(url=self.url_get_all_projects, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('数与式' in r.text)  # 获取专题包含一级专题数与式

    # 根据学科获取一级题型列表
    def test_get_insight_question_type_type_pre_by_subject(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math'}
        r = requests.get(url=self.url_get_insight_question_type_type_pre_by_subject, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('判断题' in r.text)  # 获取一级题型包含判断题

    # 根据学科标签
    def test_listTopicBySubjectEn(self):
        subject = ["math"]
        for key in subject:
            header = {'Accept': '*/*',
                      'Accept-Encoding': 'gzip, deflate, br',
                      'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                      'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                      'Connection': 'keep-alive',
                      'Content-Type': 'application/json',
                      'Host': 'zhihuotech.com',
                      'Referer': 'https://zhihuotech.com/question_bank/',
                      'Sec-Fetch-Mode': 'cors',
                      'Sec-Fetch-Site': 'same-origin',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                      'X-Requested-With': 'XMLHttpRequest'}
            r = requests.get(url=self.url_listTopicBySubjectEn.format(key), headers=header, params=None, verify=False)
            result = r.json()
            print(r.json())
            self.assertEqual(result['code'], 0)
            self.assertEqual(result['msg'], '成功')
            self.assertTrue('一元一次不等式(组)及应用' in r.text)  # 获取学科标签是一元一次不等式(组)及应用

    # 获取教材+年级接口列表
    def test_get_insight_book(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        r = requests.get(url=self.url_get_insight_book, headers=header, params=None, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('北师大版' in r.text)  # 获取学科包含北师大版

    # 根据学科和教材类型获取专题+知识点列表-树
    def test_get_point_by_book_type(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math'}
        r = requests.get(url=self.url_get_point_by_book_type, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('正比例函数的定义' in r.text)  # 获取知识点包含正比例函数的定义

    # 根据BookId获取考点列表-章节树
    def test_get_insight_book_by_id(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject_en': 'math', 'insight_book_id': 506}
        r = requests.get(url=self.url_get_insight_book_by_id, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('规律型：图形的变化类' in r.text)  # 获取章节包含规律型：图形的变化类

    # 根据学科获取所有一级题型+二级题型列表
    def test_get_question_type_by_subject(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math'}
        r = requests.get(url=self.url_get_question_type_by_subject, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('解答题' in r.text)  # 获取一级题型为解答题

    # 根据学科+一级题型获取二级题型列表
    def test_get_insight_question_type_type_by_subject(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'subject': 'math', 'typePre': 48}
        r = requests.get(url=self.url_get_insight_question_type_type_by_subject, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('填空题-复合' in r.text)  # 获取2级题型为填空-复合

    # 根据知识点ids获取所有的一级专题二级专题
    def test_get_projects_by_point_ids(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'pointId': 46113}
        r = requests.get(url=self.url_get_projects_by_point_ids, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('数与式' in r.text)  # 根据知识点获取一级题型为数与式

    # 根据知识点ids获取所有的考法
    def test_get_methods_by_point_ids(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        params_data = {'pointId': 46113}
        r = requests.get(url=self.url_get_methods_by_point_ids, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('玉莹测试6' in r.text)  # 获取知识点ID46113包含的考法为玉莹测试6

    # 提交试题
    def test_submit_question(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6aGlodW8iLCJ1c2VyX25hbWUiOiJ6aGlodW8iLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMSIsImV4cCI6MTU3NjIzNzU5MywiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX1RBR19BRE1JTiJdLCJqdGkiOiJlYmFlMzExYS1hZmE1LTQzYjQtODhkZC03ZDkyNzBhMzkwZTgiLCJjbGllbnRfaWQiOiJpbnNpZ2h0Q2xpZW50SWQiLCJzdGF0dXMiOjF9.wFfHH3NNqhVYnuiokQWG4zzmm6Z93kxM_zcaEfTHBypu5lxFxSglYIYjOxfIGBd5VnBgAmRhkQkdeu7lCNlWMFBIHv39w-l8nii7jAd9afE1-_oleffAIEyHPojG1vjqb7QRnmosTkenxVEQZOsaubRIWy0R5stAuRctLGwF5aw',
                  'Connection': 'keep-alive',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        form_data = {"analyse": "", "answers": ["的"], "cate": 2, "category_ids": [], "catename": "填空题",
                     "content": "踩踩踩踩踩<div class=\"quizPutTag\"></div>", "degree": "0.2", "discuss": "",
                     "topics": [{"key": 11713, "value": "数与式"}], "label": "", "method": "", "options": [],
                     "two_topics": [{"key": 11254, "value": "二次根式"}], "propositional_region": "全国通用",
                     "propositional_time": "2018", "questions_type": 2, "points": [
                     {"point_id": 61529, "point_name": "玉莹测试7", "point_no": "dea1f3fb-5782-4b7c-b987-246ebcc354bd",
                     "point_type": 2, "parent_point_no": "yycs", "subject_en": "math", "tag_flag": 1},
                    {"answer_order": "", "point_id": 46113, "point_name": "玉莹测试", "point_no": "yycs", "point_type": 1,
                     "subject_en": "math", "tag_flag": 1}], "pre_type": 48, "user_name": "wzg", "subject_en": "math",
                     "ques_tag": ""}
        r = requests.post(url=self.url_submit_question, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')

    # 插入试题的录入时间
    def test_insertQuestion(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Connection': 'keep-alive',
                  'Content-Length': '229',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Origin': 'https://zhihuotech.com',
                  'Referer': 'https://zhihuotech.com/question_bank/physics_add?go_show=1&username=wzg&third_subject=math&subject_name=%E6%95%B0%E5%AD%A6',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        form_data = {"ques_uuid": "b8145216-90ab-46fa-a375-6cf2c3677fd5", "subject": "math", "user_name": "wzg",
                     "cate": 2, "cate_name": "填空题", "entry_time": 442366, "start_time": "2020-04-23T05:34:59.735Z",
                     "end_time": "2020-04-23T05:42:22.101Z", "type": "1"}
        r = requests.post(url=self.url_insertQuestion, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('2020-04-23T13:34:59.735+0800' in r.text)  # 获取插入试题时间

if __name__ == '__main__':
    unittest.main()