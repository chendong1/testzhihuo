import requests
import unittest
import urllib3
# oms运营系统获取产品包列表/获取产品包有效期
class Testpackage(unittest.TestCase):
    def setUp(self):
        # 关闭SSL认证warn, 解决使用verify=False方法时warnning告警
        urllib3.disable_warnings()
        #产品包列表url
        self.url_findpackage = "https://www.zhihuotech.com/oms_back_dev/oms/productPackageManager/findPackage?"
        #产品包有效期url
        self.url_find_effective_lst = "https://www.zhihuotech.com/oms_back_dev/oms/productPackageManager/find_effective_lst"
        print("开始执行用例")
    def tearDown(self):
        print("用例执行结束")
    #获取产品包列表
    def test_findpackage(self):
        header = {
            'charset': 'utf-8',
            'content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Access-Control-Allow-Origin':'https://zhihuotech.com'
        }

        parmes_date = {
            "paqe_num": 1,
            "page_size": 10
        }
        r = requests.get(url=self.url_findpackage, params=parmes_date, headers=header, verify=False)
        result = r.json()
        print(result)
        # code为0、msg为成功、判断是否存在语文产品包
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('语文' in r.text, '验证是否存在语文产品包')

    # 获取产品包权益有效期
    def test_find_effective_lst(self):
        header = {
            'charset': 'utf-8',
            'content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Access-Control-Allow-Origin':'https://zhihuotech.com'
        }
        parmes_date = {
            None
        }
        r = requests.get(url=self.url_find_effective_lst, headers=header, verify=False)
        result = r.json()
        print(result)
        # code为0、msg为成功、返回的数据是否存在六个月的权益有效期
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'], '成功')
        self.assertTrue('六个月' in r.text, '验证是否存在六个月权益有效期')

if __name__ == '__main__':
    unittest.main()
