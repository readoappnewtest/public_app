import requests
import json
import time
#for aryan
#test datata 
file = open('test_data_2.txt','r',encoding="utf-8")
json_data = file.read()
json_js = json.loads(json_data)
n = 1
bot_url = "https://api.telegram.org/bot1568020230:AAFh3PNDg7_WbbjGh_toZSv8sqXfn6n_VVs/sendMessage?chat_id=-527297699&text=Complete "+str(n)+"data update  at"+str(time.time())+""
bot_data = requests.get(bot_url,headers={"User-Agent":"Nasa"})

for api in json_js:
    print(api['id'])
    
    try:
        print(n)
        if int(n%100) ==0:
            bot_url = "https://api.telegram.org/bot1568020230:AAFh3PNDg7_WbbjGh_toZSv8sqXfn6n_VVs/sendMessage?chat_id=-527297699&text=Complete "+str(n)+"data update  at"+str(time.time())+""
            bot_data = requests.get(bot_url,headers={"User-Agent":"Nasa"})
            n = n + 1
        else:
            n = n + 1
        #=========================================================folow=====================================================================
        
        #=========================================================================================================================

        url = "http://video-user.pix.in/v1/post/likes"
        #for amb news
        #id:FGVD1BpgT0V9iQtUulRix0xWM9J2
        #id:zecW4CqXf2ZOit4tNbQEcifAcf53#reena infotech
        #my_id =:r8Xmgyr9p8RJDuulGTT5Aaxuln02
        header= {
        "x-device-id":"5f54c935-eee1-3f92-b34d-f686561604f7",
        "x-os-type":"ANDROID",
        "x-session-count":"2",
        "x-auth-token":"m7qt41mchngg837rl8wrewg86c1611468659207",
        "x-device-name":"IPHONE",
        "x-district":"HP_UNA",
        "x-sub-district-code":"HP_UNA_GHANARI",
        "x-user-id":""+str(api['id'])+"",
        "x-child-user-id":"",
        #"x-user-token":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ4OTQ5ZDdkNDA3ZmVjOWIyYWM4ZDYzNWVjYmEwYjdhOTE0ZWQ4ZmIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQVJZQU4gSkFTV0FMIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdpaDdMMXk5ZmdlLUJmSXBLcWpuV0sxR0VWd0ktbFJaLW5lZ2NJU0ZRPXM5Ni1jIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3ZpZGVvLXNob3J0cyIsImF1ZCI6InZpZGVvLXNob3J0cyIsImF1dGhfdGltZSI6MTYxMTQ3MDE3OCwidXNlcl9pZCI6InI4WG1neXI5cDhSSkR1dWxHVFQ1QWF4dWxuMDIiLCJzdWIiOiJyOFhtZ3lyOXA4UkpEdXVsR1RUNUFheHVsbjAyIiwiaWF0IjoxNjE1NDU3NzY5LCJleHAiOjE2MTU0NjEzNjksImVtYWlsIjoiYXJ5YW5qYXN3YWxjc3BAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTM4NzI1NjE0Njg5NjI1ODQ3NjMiXSwiZW1haWwiOlsiYXJ5YW5qYXN3YWxjc3BAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.X3E3L2b5uSTQDiGu02o85WgrvFg-sn0aJs75bW5RFNhwlYAsgg86gUky1w91MNT4UDQd3815H6T6OQE6N4XazoIZoGdj2PvzrhZsTzIw_-KdoQhd5fiI5SvIaNMZnlbvnu7UjRYaHLHXQlWrTF1tu0DjTgw2b1gUHS7hC6ilDmTkULHconIauGeBvPUVO3qUt-KsQ_PFgwrXioclXUTzfYOXF9XzNBn2dfsg9IjyZfwDmV9WPvd0Pd_QPaJvcXO69NMMTDBfS_y3vobL4r9MBn9N5cF5Z0DRUqZwp_on8xWG6MjmbeWu7_ninrSwXRmi1Sh06H7DkVfzDp-LkZozMw",
        "x-latitude":"31.7484853",
        "x-longitude":"79.0676551",
        "x-network-type":"WIFI",
        "x-birth-date":"1611468656006",
        "x-manual-location":"true",
        "x-region":"IN",
        "x-selected-tenant":"HINDI",
        "x-app-version":"344",
        "x-postal-code":"177203",
        "x-admin-area":"HIMACHAL_PRADESH",
        "x-sub-admin-area":"Una",
        "x-locality":"Ghanari",
        "x-sub-district":"Ghanari",
        "x-android-id":"fda96035e26574af",
        "Host":"video-user.pix.in",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip",
        "User-Agent":"okhttp/4.9.0"
            }
        #body= '{"message":"Hiaryanj","receiver_id":"u8CU5TC9eBeongBvULTmFSlw4cY2"}'
        #body = '{"message":"Hi, hwo are you","receiver_id":"r8Xmgyr9p8RJDuulGTT5Aaxuln02"}'
        #body = '{"like_ids":["sp_cei4asxjw3ybl"],"unlike_ids":[]}'
        body = '{"like_ids":["sp_y0mgntw9k80gp"],"unlike_ids":[]}'

        data = requests.post(url,headers=header,data=body)
        print(data)
        print(data.text)
        time.sleep(5)
    
    except:
        
        
        print("Error")
        print("Error Occured")
        bot_url = "https://api.telegram.org/bot1568020230:AAFh3PNDg7_WbbjGh_toZSv8sqXfn6n_VVs/sendMessage?chat_id=-527297699&text=Error occured in server : "+str(n)+""+str(time.time())+""
        bot_data = requests.get(bot_url,headers={"User-Agent":"Nasa"})
        print(bot_data)
        time.sleep(120)
        
    
print(n)

bot_url = "https://api.telegram.org/bot1568020230:AAFh3PNDg7_WbbjGh_toZSv8sqXfn6n_VVs/sendMessage?chat_id=-527297699&text=Complete all task : "+str(n)+""+str(time.time())+""
bot_data = requests.get(bot_url,headers={"User-Agent":"Nasa"})
print(bot_data)
