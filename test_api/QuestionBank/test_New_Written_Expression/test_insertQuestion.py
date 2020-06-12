import requests
#插入试题--英语书面表达
url = 'https://zhihuotech.com/bank/questionManage/insertQuestion'
header = {'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3emciLCJ1c2VyX25hbWUiOiJ3emciLCJzY29wZSI6WyJ1c2VyX2luZm8iXSwiYWNjb3VudE9wZW5Db2RlIjoiMiIsImV4cCI6MTU4ODA1NjQxOSwiZ3JhbnRUeXBlIjoicGFzc3dvcmQiLCJhdXRob3JpdGllcyI6WyJST0xFX05BTUVfTUFUQ0giLCJST0xFX1RBR19BRE1JTiIsIlJPTEVfVVNFUiIsIlJPTEVfT01TX1VTRVIiXSwianRpIjoiYjBjYjYzNGEtNmVkOS00NmU0LWI2MzEtZTgwM2FiYmY1YWMzIiwiY2xpZW50X2lkIjoiaW5zaWdodENsaWVudElkIiwic3RhdHVzIjoxfQ.HRRtrwfM2HJ5yMVM2nthIW99tc3G4QbJ08HTSkmSDntfL8o-e1CT9lPsKxF4pAkVcUBn2Y_7b1vSKJhxQypB_mbyfKZyLUzLoK6Z9BKuRz0FdFNrwV_vDGgO6y7981ZCKBaCmpbyy7tuatfzU6EJvyPYUakqSBhncvXEA6R4pYw',
        'Connection':'keep-alive',
        'Content-Length':'1724',
        'Content-Type':'application/json',
        'Host':'zhihuotech.com',
        'Origin':'https://zhihuotech.com',
        'Referer':'https://zhihuotech.com/question_bank/add_question?go_show=1&username=wzg&third_subject=english&subject_name=%E8%8B%B1%E8%AF%AD',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
form_data = {"options_error":[],
             "question_resource_url":"",
             "listening_text":"",
             "analyse":"",
             "answers":["&nbsp; &nbsp; Li Hua spent too much time playing computer games and he fell behind others. As a good friend of his, I must do something to help him.<br>&nbsp; &nbsp; Firstly, I think it&#39;s very important for him to learn lessons well. He should spend most of his time on his study instead of computer games. Secondly, I must tell him that playing computer games too much is bad for his health, especially for his eyes. So he must give it up. I can play more sports with him after school. Maybe he will become more interested in sports than computer games. And then I&#39;ll ask him to concentrate more on his study. Of course, I will try my best to help him with all his subjects. I think I can do it in many fun ways and let him find much fun in studying. At the same time, I&#39;ll ask both his parents and our teachers to help him, too.<br>&nbsp; &nbsp; If I try these, I&#39;m sure he will make great progress soon."],
             "cate":125,
             "category_ids":["46e5cfab-28f9-481a-939b-df9b8c04e654"],
             "catename":"书面表达",
             "content":"李华沉迷于电脑游戏中，影响了学习。作为他的好朋友，你打算怎么帮他呢?请用下面所给的提示词写一篇不少于80字的短文。字迹工整，语言流畅。<br>提示词：give up concentrate on be (become)interested in",
             "degree":"0.6",
             "discuss":"",
             "topics":[],
             "label":"",
             "method":"",
             "options":[],
             "points":[{"point_id":39408,"point_name":"夹叙夹议","point_no":"","subject_en":"english","tag_flag":1},
                       {"point_id":39457,"point_name":"救护 (First aid)","point_no":"","subject_en":"english","tag_flag":2}],
             "pre_type":124,
             "user_name":"wzg",
             "subject_en":"english"}
r =  requests.post(url=url, headers=header,json=form_data,verify=False)
print(r)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))
