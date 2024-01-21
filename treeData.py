import requests   
import json   
import os


def getTreeData(ourDictionnary):
    print("Starting the collection of Tree data !")

    offset = 0
    url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=64e28fe6-ef37-437a-972d-d1d3f1f7d891&limit=9999999'  
    obj = json.loads(requests.get(url).text)
    total = obj['result']['total']
    limit = 32000


    while offset < total:
        url = f'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=64e28fe6-ef37-437a-972d-d1d3f1f7d891&limit=9999999&offset={offset}'  
        obj = json.loads(requests.get(url).text)

        for record in obj['result']['records']:

            arr = record['ARROND_NOM']

            if arr in ourDictionnary:
                if "trees" in ourDictionnary[arr]:
                    ourDictionnary[arr]['trees'] += 1
                else:
                    ourDictionnary[arr]['trees'] = 1
            else:
                ourDictionnary[arr] = {
                    "trees": 1
                }

        offset += limit
    return ourDictionnary
    