import bikeData
import requests   
import json     
from dotenv import load_dotenv
import googlemaps
import os

def getAirPollution(ourDictionnary):
    print("Starting the collection of Pollution Data !")

    offset = 0
    url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=ccd5a4b7-cbca-4f5f-a746-ad8c576af374&limit=999999'  
    obj = json.loads(requests.get(url).text)
    total = obj['result']['total']
    limit = 32000

    saved_neighborhoods = {}

    
    while offset < total:
        url = f'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=ccd5a4b7-cbca-4f5f-a746-ad8c576af374&limit=999999&offset={offset}'  
        obj = json.loads(requests.get(url).text)

        for record in obj['result']['records']:

            lat = record['latitude']
            long = record['longitude']
            
            neighborhood = ""
            if lat+long in saved_neighborhoods:
                neighborhood = saved_neighborhoods[lat + long]
            else:
                neighborhood = bikeData.get_reverse_geocode(lat, long)
                saved_neighborhoods[lat + long] = neighborhood


            if neighborhood in ourDictionnary:
                if record['polluant'] in ourDictionnary[neighborhood]:
                    pass
                else:
                    ourDictionnary[neighborhood][record['polluant']] = record['valeur']
            else:
                ourDictionnary[neighborhood] = {
                    record['polluant']: record['valeur']
                }

        offset += limit

        return ourDictionnary