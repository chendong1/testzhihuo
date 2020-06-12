import requests
#提交试题
url = 'https://zhihuotech.com/bank/questionManage/submit_question'
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
form_data = {"analyse":"","answers":["的"],"cate":2,"category_ids":[],"catename":"填空题","content":"踩踩踩踩踩<div class=\"quizPutTag\"></div>","degree":"0.2","discuss":"","topics":[{"key":11713,"value":"数与式"}],"label":"","method":"","options":[],"two_topics":[{"key":11254,"value":"二次根式"}],"propositional_region":"全国通用","propositional_time":"2018","questions_type":2,"points":[{"point_id":61529,"point_name":"玉莹测试7","point_no":"dea1f3fb-5782-4b7c-b987-246ebcc354bd","point_type":2,"parent_point_no":"yycs","subject_en":"math","tag_flag":1},{"answer_order":"","point_id":46113,"point_name":"玉莹测试","point_no":"yycs","point_type":1,"subject_en":"math","tag_flag":1}],"pre_type":48,"user_name":"wzg","subject_en":"math","ques_tag":""}
r =  requests.post(url=url, headers=header,json=form_data,verify=False)
print(r)
print(r.url)
print(type(r.content))
print(r.content.decode(encoding='utf-8'))