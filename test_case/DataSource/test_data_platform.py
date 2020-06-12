import unittest
import requests
from test_api.DataSource.test_data_platform.test_login_token import login_token
#登录到首页页面
class Data_platform(unittest.TestCase):

    def setUp(self):
        #智能练习数据分析和智能练习明细数据
        self.url_token = login_token()#获取登陆的token
        self.url_getInfo='https://shuju.zhihuotech.com/api/getInfo'#获取地区
        self.url_getBasic = 'https://shuju.zhihuotech.com/api/system/correct_overview/record/getBasic'#数据分析顶部数据展示
        self.url_getTrend='https://shuju.zhihuotech.com/api/system/correct_overview/record/getTrend'#智能练习时间范围内数据展示
        self.url_getCurrentUserArea='https://shuju.zhihuotech.com/api/system/user/getCurrentUserArea'#使用明细获取地址
        self.url_get_current_user_school='https://shuju.zhihuotech.com/api/system/smart_exercise_detail/get_current_user_school'#获取学校名单
        self.url_get_log_exam_batch_detail='https://shuju.zhihuotech.com/api/system/smart_exercise_detail/get_log_exam_batch_detail'#组题老师数
        self.url_get_teacher_print_detail='https://shuju.zhihuotech.com/api/system/smart_exercise_detail/get_teacher_print_detail'#打印教师数
        self.url_get_teacher_report_detail='https://shuju.zhihuotech.com/api/system/smart_exercise_detail/get_teacher_report_detail'#批改教师数
        self.url_get_student_report_detail='https://shuju.zhihuotech.com/api/system/smart_exercise_detail/get_student_report_detail'#批改学生数
        print ('开始执行用例')

    def tearDown(self):
        print("用例结束")

    #获取地区
    def test_url_getInfo(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.get(url=self.url_getInfo, headers=header, params=None, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('山西测试销售' in r.text, '首页接口失败')#获取字段deptName

    #数据分析顶部数据展示
    def test_url_getBasic(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.get(url=self.url_getBasic, headers=header, params=None, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('组题教师数' in r.text, '首页接口失败')#获取返回的字段name的值

    # #智能练习时间范围内数据展示
    def test_url_getTrend(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }
        params_data = {'timeType': '1',
                       'startDate': '2020-04-21',
                       'endDate': '2020-04-21'}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.get(url=self.url_getTrend, headers=header, params=params_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('打印教师数' in r.text, '首页接口失败')#获取字段name

    #使用明细获取地址
    def test_getCurrentUserArea(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.get(url=self.url_getCurrentUserArea, headers=header, params=None, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('河南省' in r.text, '首页接口失败')#获取province字段

    #获取学校名单
    def test_get_current_user_school(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.post(url=self.url_get_current_user_school, headers=header, data=None, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('菜园路初级中学' in r.text, '首页接口失败')#验证返回data中是否包含正确的学校名称

    #组题老师数
    def test_get_log_exam_batch_detail(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        form_data = {"page": 1, "pageSize": 10, "province": "", "city": "", "school": "", "batchId": "", "subject": "",
                     "teacherName": "", "studentName": "", "dateLimitBegin": "2020-04-09", "dateLimitEnd": "2020-04-23"}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.post(url=self.url_get_log_exam_batch_detail, headers=header, json=form_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('菜园路初级中学' in r.text, '首页接口失败')#验证返回数据中是否包含正确的学校名称

    #打印教师数
    def test_get_teacher_print_detail(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        form_data = {"page": 1, "pageSize": 10, "province": "", "city": "", "school": "", "batchId": "", "subject": "",
                     "teacherName": "", "studentName": "", "dateLimitBegin": "2020-04-09", "dateLimitEnd": "2020-04-23"}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.post(url=self.url_get_teacher_print_detail, headers=header, json=form_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('菜园路初级中学' in r.text, '首页接口失败')#验证返回数据中是否包含正确的学校名称

    #批改老师数
    def test_get_teacher_report_detail(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/analysis',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }

        form_data = {"page": 1, "pageSize": 10, "province": "", "city": "", "school": "", "batchId": "", "subject": "",
                     "teacherName": "", "studentName": "", "dateLimitBegin": "2020-04-09", "dateLimitEnd": "2020-04-23"}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.post(url=self.url_get_teacher_report_detail, headers=header, json=form_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('菜园路初级中学' in r.text, '首页接口失败')#验证返回school_name是否包含正确的学校名称

    #批改学生数
    def test_get_student_report_detail(self):
        header = {
            'Host': 'shuju.zhihuotech.com',
            'Connection': 'keep-alive',
            'Content-Length': '178',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer {}'.format(self.url_token),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://shuju.zhihuotech.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://shuju.zhihuotech.com/business/detail',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
        }
        form_data = {"page": 1, "pageSize": 10, "province": "", "city": "", "school": "", "batchId": "", "subject": "",
                     "teacherName": "", "studentName": "", "dateLimitBegin": "2020-04-07", "dateLimitEnd": "2020-04-21"}
        requests.packages.urllib3.disable_warnings()  # 去除警示提示
        r = requests.post(url=self.url_get_student_report_detail, headers=header, json=form_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'], 200, '首页接口失败')
        self.assertEqual(resuit['msg'], '操作成功', '首页接口失败')
        self.assertTrue('登封市区第三初级中学' in r.text, '首页接口失败')#

if __name__=='__main__':
    unittest.main()