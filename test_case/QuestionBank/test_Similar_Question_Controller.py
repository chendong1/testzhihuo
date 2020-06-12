import json
import unittest
import requests
class TestSimilar_Question_Controller(unittest.TestCase):

    #相似试题查询标记
    def setUp(self):
        self.url_disSimilarQuestion = 'https://zhihuotech.com/bank/similarQuestion/disSimilarQuestion'
        self.url_listSimilarQuestion= 'https://zhihuotech.com/bank/similarQuestion/listSimilarQuestion'
    print('开始执行用例')

    # 相似试题标记
    def test_disSimilarQuestion(self):
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
                  'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        form_data = {'similar_question_id': '56666'}
        r = requests.post(url=self.url_disSimilarQuestion, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('1' in r.text)  # 非相似标记成功

    # 相似试题查询
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
        form_data = {'cate': 125,
                     'page_num': 1,
                     'question_uuid': '0c69e7bf-73b2-42c6-a630-61a871e4b488',
                     'subject': 'english'}
        r = requests.post(url=self.url_listSimilarQuestion, headers=header, json=form_data, verify=False)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('李华沉迷于电脑游戏中，影响了学习。' in r.text)  # 相似题的题干包含李华沉迷于电脑游戏中，影响了学习。

if __name__ == '__main__':
    unittest.main()