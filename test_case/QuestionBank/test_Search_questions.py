import unittest
import requests

class Search_question(unittest.TestCase):
    def setUp(self):

#搜索试题可以查看并更改标记

        self.url_insight_book='https://zhihuotech.com/bank/knowledge_external_api/get_insight_book'
        self.url_insight_book_id='https://zhihuotech.com/bank/knowledge_external_api/get_insight_book_by_id'
        self.url_question_type_subject='https://zhihuotech.com/bank/questionManage/get_question_type_by_subject'
        self.url_math_physics_chemistry_ques='https://zhihuotech.com/bank/ques_bank/math_physics_chemistry_ques'
        self.url_search_uuid_questions='https://zhihuotech.com/bank/questionManage/getOneQuestionById/9a00628b-bbae-4e7d-8f09-17a5aa088265'
        self.url_search_for_bank='https://zhihuotech.com/bank/questionSearch/search_for_bank'
        self.url_ques_tag='https://zhihuotech.com/bank/ques_bank/ques_tag'
        print('开始执行用例')

    def tearDown(self):
        print('用例结束')

        # 获取科目

    def test_insight_book(self):
            header = {
                'Accept-Encoding': 'gzip'  'deflate'  'br',
                'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODczNTk5MCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTRkMjRhODItYjQxMi00NDc0LThmMTEtZWU2NTYxM2RmMzZmIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.MEytqpo2i1m3G0qmmEJpdNjEGA-mFjzTTMxJFgcT2IL4-EA2kAzyrLNRQ_rau9YohOoAlPd1rC-puu2Lbjri6fH4R_CO6ZxFMlA7kgWfulz-8NpuOjAcpfpOuKLzdKbi1o_Kf9gZubFRKbZXXZCzCA7_JdQDIU4MvXhTFTt8A2A',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Host': 'zhihuotech.com',
                'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }
            Params_data = {}
            r = requests.get(url=self.url_insight_book, params=Params_data, headers=header, verify=False)
            result = r.json()
            print(r.text)

            self.assertEqual(result['code'], 0)
            self.assertEqual(result['msg'], '成功')
            self.assertTrue('chemistry' in r.text)  # 查看学科名称

        #获取教材id

    def test_insight_book_id(self):
            header = {
                'Accept-Encoding': 'gzip'  'deflate'  'br',
                'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODczNTk5MCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTRkMjRhODItYjQxMi00NDc0LThmMTEtZWU2NTYxM2RmMzZmIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.MEytqpo2i1m3G0qmmEJpdNjEGA-mFjzTTMxJFgcT2IL4-EA2kAzyrLNRQ_rau9YohOoAlPd1rC-puu2Lbjri6fH4R_CO6ZxFMlA7kgWfulz-8NpuOjAcpfpOuKLzdKbi1o_Kf9gZubFRKbZXXZCzCA7_JdQDIU4MvXhTFTt8A2A',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Host': 'zhihuotech.com',
                'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }
            Params_data = {'insight_book_id': '624'}
            r = requests.get(url=self.url_insight_book_id, params=Params_data, headers=header, verify=False)
            result = r.json()
            print(r.text)

            self.assertEqual(result['code'], 0)
            self.assertEqual(result['msg'], '成功')
            self.assertTrue('465' in r.text) # id是465

        #获取科目和题型

    def test_question_type_subject(self):
            header = {
                'Accept-Encoding': 'gzip'  'deflate'  'br',
                'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                'Connection': 'keep-alive',
                'Host': 'zhihuotech.com',
                'Referer': 'https://zhihuotech.com/question_bank/questionshow?username=wzg',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
             }
            Params_data = {'subject': 'chemistry'}
            r = requests.get(url=self.url_question_type_subject, params=Params_data, headers=header, verify=False)
            result = r.json()
            print(r.text)

            self.assertEqual(result['code'], 0)
            self.assertEqual(result['msg'], '成功')
            self.assertTrue('43' in r.text) # id是43

        #获取数理化学科

    def test_math_physics_chemistry_ques(self):
            header = {
                'Accept-Encoding': 'gzip'  'deflate'  'br',
                'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODczNTk5MCwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYTRkMjRhODItYjQxMi00NDc0LThmMTEtZWU2NTYxM2RmMzZmIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.MEytqpo2i1m3G0qmmEJpdNjEGA-mFjzTTMxJFgcT2IL4-EA2kAzyrLNRQ_rau9YohOoAlPd1rC-puu2Lbjri6fH4R_CO6ZxFMlA7kgWfulz-8NpuOjAcpfpOuKLzdKbi1o_Kf9gZubFRKbZXXZCzCA7_JdQDIU4MvXhTFTt8A2A',
                'Connection': 'keep-alive',
                'Content-Length': '325',
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
            form_data = {
                'cate': '1',
                'page_num': '1',
                'page_size': '10',
                'point_no': 'e1',
                'subject': 'chemistry',
                'ques_tag': '4',
                'user_id': '1',
                'tag_flag': '0',
                'point_count_lst': [],
                'degree_lst': [],
                'point_behind': '0',
                'third_category_id': 'a66ccdf0-c610-46c3-919d-1ad9a7041155',
                'insight_book_id': '624',
                'question_type_list': [],
                'propositional_time_list': [],
                'point_id': '12460',
            }
            r = requests.post(url=self.url_math_physics_chemistry_ques, headers=header, json=form_data, verify=False)
            result = r.json()
            print(r.json())

            self.assertEqual(result['code'], 0)
            self.assertEqual(result['msg'], '成功')
            #self.assertTrue('null' in r.text) #输出null

            #输入uuid搜索试题

    def test_search_uuid_questions(self):
            header = {
                'Accept-Encoding': 'gzip' 'deflate' 'br',
                'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                'Connection': 'keep-alive',
                'Content-Length': '2',
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
            form_data = {
            }
            r = requests.post(url=self.url_search_uuid_questions, headers=header, json=form_data, verify=False)
            result = r.json()
            print(r.json())

            self.assertEqual(result['code'], 0)
            self.assertEqual(result['msg'], '成功')
            self.assertTrue( '435239' in r.text) #查看id是435239

            #按试题内容搜索

    def test_search_for_bank(self):
                header = {
                    'Accept-Encoding': 'gzip' 'deflate' 'br',
                    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Length': '183',
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
                form_data = {
                    'wd': '若一个三角形中有一个角是直角',
                    'search_id': ' ',
                    'subject': 'math',
                    'types': [9],
                    'chapters': [],
                    'points': [],
                    'page_num': 1,
                    'page_size': 10,
                    'filter_uuids': [],
                    'ques_tags': [1],
                }

                r = requests.post(url=self.url_search_for_bank, headers=header, json=form_data, verify=False)
                result = r.json()
                print(r.json())

                self.assertEqual(result['code'], 0)
                self.assertEqual(result['msg'], '成功')
                self.assertTrue('5497' in r.text) #搜索出来的试题总页数是550

            # 更改试题状态
    def test_ques_tag(self):
                header = {
                    'Accept-Encoding': 'gzip' 'deflate' 'br',
                    'Accept-Language': 'zh-CN' 'zh' 'q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Length': '193',
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
                form_data = {
                    'wd': '若一个三角形中有一个角是直角',
                    'search_id': ' ',
                    'subject': 'math',
                    'types': [9],
                    'chapters': [],
                    'points': [],
                    'page_num': 1,
                    'page_size': 10,
                    'filter_uuids': [],
                    'ques_tags': [1]
                }
                r = requests.post(url=self.url_search_for_bank, headers=header, json=form_data, verify=False)
                result = r.json()
                print(r.text)

                self.assertEqual(result['code'], 0)
                self.assertEqual(result['msg'], '成功')
                self.assertTrue('null' in r.text) #数据值为null
if __name__ == '__main__':
    unittest.main()



