import requests   
import json     

def getBikeData(ourDictionnary):
    offset = 0
    url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=65a37da8-a7cf-4812-a3b5-5edff31c45f6&limit=9999999'  
    obj = json.loads(requests.get(url).text)
    total = obj['result']['total']
    limit = 32000


    while offset < total:
        url = f'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=65a37da8-a7cf-4812-a3b5-5edff31c45f6&limit={limit}&offset={offset}'  
        obj = json.loads(requests.get(url).text)

        for record in obj['result']['records']:
            print(record)

        offset += limit
    
    
    return 0

getBikeData(None)