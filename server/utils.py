'''
    This file contains the utility functions which interact with the server through the rest api of the server
'''

import json
import requests

url = 'http://127.0.0.1:5000/'

def to_json(table_datas):

    res = []

    for table_data in table_datas:
        res.append(json.dumps(table_data))

    return res


def insert(table_datas):
    
    '''
        Takes in the tuple as dictionary
        Inserting new values from ui to the server using the api
        raises error if unable to insert the tuple
        
        table_data : dict(table_name: string, value: dict )

        value : the the row which is tobe inserted in table_name table.
        
        table_datas = list(table_data)

        for eg. table_datas = [ 
                                {'table_name':'cities', 'value': {'city_id':123, 'city_name':"'New York City'", 'city_state':"'New York'"}},
                                {'table_name':'cities', 'value': {'city_id':321, 'city_name':"'Trenton'", 'city_state':"'New Jersey'"}}
                            ]
    '''

    response = requests.post(url, data={'data': to_json(table_datas)})

    if response.status_code == 202:
        return {'OK':True}
    
    else:
        return {'OK':False, 'status_code': response.status_code,'reason':response.json()['reason']}


def show(table_name):

    '''
    As we have single table dummy DBMS just does `SELECT * FROM cities;`
    '''
    response = requests.get(url, data = {'data':table_name})
    
    if response.status_code == 202:
        return {'OK':True,'result':response.json()['result']}
    
    else:
        return {'OK':False}