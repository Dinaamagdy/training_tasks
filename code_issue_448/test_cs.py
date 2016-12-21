import multiprocessing
import threading
import requests
import json
import time

urllog= 'https://du-conv-2.demo.greenitglobe.com/restmachine/system/usermanager/authenticate'
url_creat_cs='https://du-conv-2.demo.greenitglobe.com/restmachine//cloudapi/cloudspaces/create'
url_get_cs_status='https://du-conv-2.demo.greenitglobe.com/restmachine//cloudapi/cloudspaces/get'
Data_log={'name':'Dina2','secret':'dinamagdy'}
Data_creat_cs ={ 'accountId':'359','location':'du-conv-2','name':csname,'access':'ahmed'}
def rand_str(size=6):
    chars=string.ascii_lowercase + string.hexdigits
    return [''.join(random.choice(chars) for _ in range(size)) for _ in range(4) ]

def create_cs(csname):
    session= requests.Session()
    response=session.post(urllog,data=Data_log)
    if response.status_code == 200 :
        response=session.post(url=url_creat_cs,data=Data_creat_cs)
        if response.status_code == 200 :
            time.sleep(10)
            cs_id = response.text
            print cs_id
            cs_data = {'cloudspaceId': cs_id}
            status = 'NAND'
            while status != 'DEPLOYED':
                try:
                    content = session.post(url=url_get_cs_status, data=cs_data)
                except Exception ,e:
                    print(e.msg)
                else:
                    resp = json.loads(content.text)
                    status = resp['status']
                    time.sleep(10)
            print csname, " : ", status
cs_names = rand_str(2)
for v in cs_names:
    p = multiprocessing.Process(target=create_cs, args=(v,))
    p.start()
