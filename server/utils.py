'''
    This file contains the utility functions which interact with the server through the rest api of the server
'''

import json
import requests

url = 'http://127.0.0.1:5000/'


def insert(data):
    
    '''
        Takes in the tuple as dictionary
        Inserting new values from ui to the server using the api
        raises error if unable to insert the tuple
    '''

    response = requests.post(url, data=data)

    if response.status_code == 202:
        return {'OK':True}
    
    else:
        return {'OK':False, 'status_code': response.status_code,'reason':response.json()['reason']}


def show():

    '''
    As we have single table dummy DBMS just does `SELECT * FROM cities;`
    '''
    response = requests.get(url)
    
    if response.status_code == 202:
        return {'OK':True,'result':response.json()['result']}
    
    else:
        return {'OK':False}