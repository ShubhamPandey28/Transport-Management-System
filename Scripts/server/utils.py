import json
import requests

url = 'http://127.0.0.1:5000/'

def to_json(table_datas):
    
    return list(map(json.dumps, table_datas))


def string_arg(arg1):
    return ("'" + arg1 + "'")

def convertKeys(data):
    new_data = []
    for row in data:
        new_dict = {}
        for key, val in row.items():
            new_dict['`' + key + '`'] = val

        new_data.append(new_dict)

    return new_data

def insert(table_name, rows):
    table_data = []
    if (type(rows) == type(table_data)):
        table_data = rows
    else:
        table_data.append(rows)
    
    table_data = convertKeys(table_data)

    response = requests.post(url + table_name, data={'data': to_json(table_data)})

    if response.status_code == 202:
        return {'OK':True}
    
    else:
        return {'OK':False, 'status_code': response.status_code,'reason':response.json()['reason']}


def get_table(table_name):
    response = requests.get(url + table_name)
    
    if response.status_code == 202:
        return {'OK':True,'result':response.json()['result']}
    
    else:
        return {'OK':False}
    