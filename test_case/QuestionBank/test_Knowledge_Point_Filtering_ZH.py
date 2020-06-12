import json
import unittest
import requests
class TestKnowledge_Point_Filtering_ZH(unittest.TestCase):
    #知识点去掉“zh”调用的相关接口
    def setUp(self):
        self.url_get_insight_book='https://zhihuotech.com/devj/get_insight_book_by_id/grade/{}/subject_id/{}/insight_book_id/{}'
        self.url_get_unified_new = 'https://zhihuotech.com/devj/applet/examination/get_unified_new'
        self.url_getSpecialTopic = 'https://zhihuotech.com/devj/applet/crate_examination/getSpecialTopic'
        self.url_previewByTopic= 'https://zhihuotech.com/devj/applet/crate_examination/previewByTopic'
        self.url_preview_v2= 'https://zhihuotech.com/devj/applet/crate_examination/unified/preview/v2'
    print('开始执行用例')

    # 出题专题列表页接口
    def test_get_insight_book(self):
        grade = 8
        subject_id = 2
        insight_book_id = 467
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
        r = requests.get(url= self.url_get_insight_book.format(grade,subject_id,insight_book_id), headers=header, params=None, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('二元一次方程组的解' in r.text)  # 获取知识点为二元一次方程组的解

    # 同步/专题出题后查看试题
    def test_get_unified_new(self):
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
        params_data = {'union_id': 'oyu3N0c42gIBsIUrayCFnV9JbpGo', 'class_id': '31410007232205170',
                       'batch_id': '2020050612422681812'}
        r = requests.get(url=self.url_get_unified_new, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('二元一次方程组的解' in r.text)  # 获取知识点为二元一次方程组的解

    # 出题专题列表页接口
    def test_getSpecialTopic(self):
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
        params_data = {'subject': '2', 'class_id': '31410007232205170'}
        r = requests.get(url=self.url_getSpecialTopic, headers=header, params=params_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('二元一次方程组的解' in r.text)  # 获取知识点为二元一次方程组的解

    # 专题组题：预览
    def test_previewByTopic(self):
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
        form_data = {"question_num_vos": [{"cate": "2", "question_num": 8, "question_count_num": 24}],
                     "class_id": "31410007232205170",
                     "subject": "2",
                     "create_union_id": "oyu3N0c42gIBsIUrayCFnV9JbpGo",
                     "book_id": "46be896b-5a89-434b-bf45-26dc7ed43ecd",
                     "category_ids": [""],
                     "point_nos": [""],
                     "point_ids": ["54003"]}
        r = requests.post(url=self.url_previewByTopic, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('二元一次方程组的解' in r.text)  # 获取知识点为二元一次方程组的解

    # 统一组题：预览
    def test_preview_v2(self):
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
        form_data = {"question_num_vos": [{"cate": "2", "question_num": 8, "question_count_num": 24}],
                     "class_id": "31410007232205170",
                     "subject": "2",
                     "create_union_id": "oyu3N0c42gIBsIUrayCFnV9JbpGo",
                     "book_id": "46be896b-5a89-434b-bf45-26dc7ed43ecd",
                     "category_ids": [""],
                     "point_nos": [""],
                     "point_ids": ["54003"]}
        r = requests.post(url=self.url_preview_v2, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('二元一次方程组的解' in r.text)  # 获取知识点为二元一次方程组的解

if __name__ == '__main__':
    unittest.main()