import requests
import unittest


# 小程序老师和家长端查看批改报告及详情
class TestFencengfufei(unittest.TestCase):
    # 准备url
    def setUp(self) :
        # 小程序老师和家长端查看批改报告及详情url
        self.url_test_parent_overview = "http://152.136.226.216:8198/report/parent/overview"
        self.url_test_parent_detail = "http://152.136.226.216:8198/report/parent/detail"
        self.url_test_teacher_overview = "http://152.136.226.216:8198/report/teacher/overview"
        self.url_test_teacher_detail = "http://152.136.226.216:8198/report/teacher/detail"
        print("开始执行用例")

    def tearDown(self) :
        print("用例结束")

    # 家长查看批改报告预览
    def test_parent_overview(self) :
        header = {
            'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            'content-type' : 'application/json',
            'Host' : 'zhihuotech.com',
            'Pragma' : 'no-cache',
            'Referer' : 'https://servicewechat.com/wx358a536fed195cc8/devtools/page-frame.html',
            'Sec-Fetch-Dest' : 'empty',
            'Sec-Fetch-Site' : 'cross-site',
            'Sec-Fetch-User' : '?F',
            'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'
        }
        params_data = {'batch_id' : '2020042413330354377', 'class_id' : '31410007232205203', 'student_id' : '226384'}
        r = requests.get(url=self.url_test_parent_overview, headers=header, params=params_data)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], "成功")
        self.assertTrue('43.8' in r.text, '学生成绩不是43.8分')  # 验证学生此次考试得分

    # 家长查看家长报告预览-学情诊断详情
    def test_parent_detail(self) :
        header = {
            'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            'content-type' : 'application/json',
            'Host' : 'zhihuotech.com',
            'Pragma' : 'no-cache',
            'Referer' : 'https://servicewechat.com/wx358a536fed195cc8/devtools/page-frame.html',
            'Sec-Fetch-Dest' : 'empty',
            'Sec-Fetch-Site' : 'cross-site',
            'Sec-Fetch-User' : '?F',
            'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'
        }
        params_data = {
            'batch_id' : '2020042413330354377',
            'class_id' : '31410007232205203',
            'student_id' : '226384',
            'template_id' : '1',
            'question_ids' : '396006'
        }
        r = requests.get(url=self.url_test_parent_detail, params=params_data, headers=header)
        result = r.json()
        print(r.json())

        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('6.0' in r.text, '学生学情诊断详情不是6.0分')  # 判断学生学情诊断详情是否可以正常显示

    # 老师查看批改报告预览
    def test_teacher_overview(self) :
        header = {
            'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            'content-type' : 'application/json',
            'Host' : 'zhihuotech.com',
            'Pragma' : 'no-cache',
            'Referer' : 'https://servicewechat.com/wx358a536fed195cc8/devtools/page-frame.html',
            'Sec-Fetch-Dest' : 'empty',
            'Sec-Fetch-Site' : 'cross-site',
            'Sec-Fetch-User' : '?F',
            'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'
        }
        params_data = {
            'batch_id' : '2020042903290704466',
            'class_id' : '31410007232205203',
            'type' : '1'
        }
        r = requests.get(url=self.url_test_teacher_overview, headers=header, params=params_data)
        result = r.json()
        print(r.json())
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('97.1' in r.text, '班级平均分不是97.1')  # 断言看下老师端是否显示班级平均分

    def test_teacher_detail(self) :
        header = {
            'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            'content-type' : 'application/json',
            'Host' : 'zhihuotech.com',
            'Pragma' : 'no-cache',
            'Referer' : 'https://servicewechat.com/wx358a536fed195cc8/devtools/page-frame.html',
            'Sec-Fetch-Dest' : 'empty',
            'Sec-Fetch-Site' : 'cross-site',
            'Sec-Fetch-User' : '?F',
            'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'
        }
        params_data = {
            'batch_id' : '2020042903290704466',
            'class_id' : '31410007232205203',
            'tempalte_id' : '2',
            'question_ids' : '555866,555860,555877',
        }
        r = requests.get(url=self.url_test_teacher_detail, headers=header, params=params_data)
        result = r.json()
        print(r.json())

        self.assertEqual(result['code'], 0)
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('91.7' in r.text, '第5题得分率不是91.7')  # 断言第5题的得分率是否为91.7

if __name__=='__main__':
    unittest.main()
