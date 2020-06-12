import json
import unittest
import requests
class TestAreaCleaning(unittest.TestCase):

    # 清洗地区后调用相关接口
    def setUp(self):
        self.url_get_question_by_uuid = 'https://zhihuotech.com/bank/questionManage/get_question_by_uuid/{}'
        self.url_get_areas = 'https://zhihuotech.com/bank/question_area/get_areas'
        self.url_math_physics_chemistry_ques= 'https://zhihuotech.com/bank/ques_bank/math_physics_chemistry_ques'
        self.url_listSimilarQuestion= 'https://zhihuotech.com/bank/similarQuestion/listSimilarQuestion'

    print('开始执行用例')

    # 根据UUID查询试题，返回该题的地区
    def test_get_question_by_uuid(self):
        uuid = "ca914e77-15d0-4ea9-a13e-e857fea53bb1"
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
        form_data = {'UUID': "ca914e77-15d0-4ea9-a13e-e857fea53bb1"}
        r = requests.post(url=self.url_get_question_by_uuid.format(uuid),headers=header,json=form_data,verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('北京城区' in r.text)  # 获取地区为北京城区

    #地区接口
    def test_get_areas(self):
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
        r = requests.get(url=self.url_get_areas, headers=header, params=None, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('全国通用' in r.text)  # 获取地区为全国通用

    #知识点查询试题列表返回的地区
    def test_math_physics_chemistry_ques(self):
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
        form_data = {"cate": 1,
                     "page_num": 1,
                     "page_size": 10,
                     "point_no": "81",
                     "subject": "math",
                     "ques_tag": 4,
                     "user_id": 1,
                     "tag_flag": 0,
                     "point_count_lst": [],
                     "degree_lst": [],
                     "point_behind": "0",
                     "third_category_id": "68f53697-974b-4ebb-97c5-8832fd7b60c0",
                     "insight_book_id": 506,
                     "question_type_list": [],
                     "propositional_time_list": [],
                     "only_similar": 0,
                     "point_id": "11255"}
        r = requests.post(url=self.url_math_physics_chemistry_ques, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('吕梁市' in r.text)  # 获取某一到题地区为吕梁市
    def test_listSimilarQuestion(self):
        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODkyMjE0NCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiNTVmMWQ4N2ItM2ZmOC00MDNhLThiMGEtNDBiODJmZTVlZTg5IiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.tKeI9T8DWb4O-y84UMu1OFfKAqapIRpzycjmT5lyoeqIX9aaSNsArKjePQoysUOc3h8g5IsujLMj7JkVJcPJnJEFlpqrlo6j72xsqpjs-804Cetlf0oJEq3YLaAobsggtY5ekwp_rds2Fu57fYFZR1ocpLRzfM-cOWR2RBwgT48',
                  'Cache-Control': 'no-cache',
                  'Connection': 'keep-alive',
                  'Content-Length': '321',
                  'Content-Type': 'application/json',
                  'Host': 'zhihuotech.com',
                  'Origin': 'https://zhihuotech.com',
                  'Pragma': 'no-cache',
                  'Referer': 'https://zhihuotech.com/question_bank/same_question?pre_type=124&tiuuid=0c69e7bf-73b2-42c6-a630-61a871e4b488&subject=english&cate=125&ques_tag=1&similar_question_id=null',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        form_data = {"cate":"2",
                     "page_num":1,
                     "question_uuid":"124e98de-3dd2-429e-87d0-0c97d3450377",
                     "subject":"physics"}
        r = requests.post(url=self.url_listSimilarQuestion, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('福建省' in r.text)  # 获取某一到题地区为福建省