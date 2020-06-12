import unittest
import requests

#登录到首页页面
class TestLogin(unittest.TestCase):

    def setUp(self):
        #登录到首页所有链接
        self.url_cardInfo='https://zhihuotech.com/devj/applet/cardInfo'
        self.url_is_new = 'https://zhihuotech.com/devj/chk/is_new'
        print ('开始执行用例')

    def tearDown(self):
        print("用例结束")

    #登录到首页选择学校和任课教师班级页面
    def test_cardInfo(self):
        header = {
            'charset': 'utf-8',
            'Accept-Encoding': 'gzip',
            'referer': 'https://servicewechat.com/wx358a536fed195cc8/0/page-frame.html',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MicroMessenger/7.0.9.1560(0x27000934) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
            'Content-Length': '107',
            'Host': 'zhihuotech.com',
            'Connection': 'Keep-Alive'
        }
        form_data= {'class_id': '31410007232205208',
                  'role': '0',
                  'student_id': '',
                  'union_id': 'oyu3N0X-jvsSabhqSPhCQd42yZ-A',
                  'page_num': '1',
                  'page_size': '10'
                  }
        r = requests.post(url=self.url_cardInfo, headers=header, data=form_data, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'],0,'首页接口失败')
        self.assertEqual(resuit['msg'],'成功','首页接口失败')
        self.assertTrue('31410007232205208' in r.text,'首页接口失败')#验证返回结果中的class_id是否在文本中

    #获取班级列表
    def test_is_new(self):
        header = {
            'charset': 'utf-8',
            'Accept-Encoding': 'gzip',
            'referer': 'https://servicewechat.com/wx358a536fed195cc8/0/page-frame.html',
            'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MicroMessenger/7.0.9.1560(0x27000934) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
            'Host': 'zhihuotech.com',
            'Connection': 'Keep-Alive'
        }
        params_data = {'union_id': 'oyu3N0X-jvsSabhqSPhCQd42yZ-A'}
        r = requests.get(url=self.url_is_new, params=params_data, headers=header, verify=False)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'],0,'首页接口失败')
        self.assertEqual(resuit['msg'],'成功','首页接口失败')
        self.assertTrue('31410007232205156' in r.text,'首页接口失败')#验证返回结果中的class_id是否在文本中

if __name__=='__main__':
    unittest.main()