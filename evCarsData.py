import json
import requests
import os
import bikeData

def getEvCarsData(ourDictionnary):
    print("Starting the collection of Cars data !")
    limit = 32000
    offset = 0
    url = f'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=f82f00c0-baed-4fa1-8b01-6ed60146d102&limit={limit}'  
    obj = json.loads(requests.get(url).text)
    total = obj['result']['total']
    
    saved_neighborhoods = {}

    amt_of_days = 1
    curr_date = obj['result']['records'][0]['Date']

    all_cars = 0

    while offset < total:
        url = f'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=f82f00c0-baed-4fa1-8b01-6ed60146d102&limit={limit}&offset={offset}'  
        obj = json.loads(requests.get(url).text)

        for record in obj['result']['records']:

            lat = record['Longitude']
            long = record['Latitude']
            

            if record['Date'] != curr_date:
                    curr_date = record['Date']
                    amt_of_days += 1

            neighborhood = ""

            if lat+long in saved_neighborhoods:
                 neighborhood = saved_neighborhoods[lat + long]
            else:
                neighborhood = bikeData.get_reverse_geocode(record['Latitude'], record['Longitude'])
                saved_neighborhoods[lat + long] = neighborhood


            if record['Description_Code_Banque'] == "Autos":
                all_cars += int(record["NBLT"]) + int(record['NBT']) + int(record['NBRT']) + int(record['SBLT']) + int(record['SBT']) + int(record['SBRT']) + int(record['EBLT']) + int(record['EBT']) + int(record['EBRT']) + int(record["WBLT"]) + int(record['WBT']) + int(record['WBRT'])
            
                if neighborhood in ourDictionnary:
                    if 'cars' in ourDictionnary[neighborhood]:
                        ourDictionnary[neighborhood]['cars'] += all_cars
                    else:
                        ourDictionnary[neighborhood]['cars'] = all_cars
                else:
                    ourDictionnary[neighborhood] = {}
                    ourDictionnary[neighborhood]['cars'] = all_cars

        offset += limit

        for key in ourDictionnary:
         if 'cars' in ourDictionnary[key]:
            ourDictionnary[key]['cars'] = int(ourDictionnary[key]['cars'] / amt_of_days)            
    return ourDictionnary
