import json
import requests

url = 'http://127.0.0.1:5000/'

def to_json(table_datas):
    
    return list(map(json.dumps, table_datas))


def insert(table_name, table_data):
    response = requests.post(url, data={'data': to_json(table_data)})

    if response.status_code == 202:
        return {'OK':True}
    
    else:
        return {'OK':False, 'status_code': response.status_code,'reason':response.json()['reason']}


def show(table_name, to_disp=None):
    response = requests.get(url, data = {'data':json.dumps(to_disp)})
    
    if response.status_code == 202:
        return {'OK':True,'result':response.json()['result']}
    
    else:
        return {'OK':False}
    