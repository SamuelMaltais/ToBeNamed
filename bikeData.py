import requests   
import json     
from dotenv import load_dotenv
import googlemaps
import os


def get_reverse_geocode(lat, long):
    load_dotenv()
    gmap_key = os.getenv('GOOGLE_KEY')
    gmaps = googlemaps.Client(key=gmap_key)

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((lat, long))
    arrondissement = reverse_geocode_result[0]['address_components'][2]['long_name']

    return arrondissement




def getBikeData(ourDictionnary):
    offset = 0
    url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=65a37da8-a7cf-4812-a3b5-5edff31c45f6&limit=9999999'  
    obj = json.loads(requests.get(url).text)
    total = obj['result']['total']
    limit = 32000

    amt_of_days = 1
    curr_date = obj['result']['records'][0]['date']

    print("Starting the collection of Bike Data")

    saved_neighborhoods = {}

    while offset < total:
        url = f'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=65a37da8-a7cf-4812-a3b5-5edff31c45f6&limit={limit}&offset={offset}'  
        obj = json.loads(requests.get(url).text)

        for record in obj['result']['records']:
            if record['date'] != curr_date:
                    curr_date = record['date']
                    amt_of_days += 1

            lat = record['latitude']
            long = record['longitude']

            neighborhood = ""

            if lat+long in saved_neighborhoods:
                 neighborhood = saved_neighborhoods[lat + long]
            else:
                neighborhood = get_reverse_geocode(record['latitude'], record['longitude'])
                saved_neighborhoods[lat + long] = neighborhood

            if neighborhood == "Ahuntsic-Cartierville":
                 neighborhood = "Ahuntsic - Cartierville"

            if neighborhood == "Villeray—Saint-Michel—Parc-Extension":
                 neighborhood = "Villeray-Saint-Michel - Parc-Extension"

            if neighborhood in ourDictionnary:
                 ourDictionnary[neighborhood]['bikes'] += int(record['nb_passages'])
            else:
                 ourDictionnary[neighborhood] = {}
                 ourDictionnary[neighborhood]['bikes'] = int(record['nb_passages'])


        offset += limit
    
    
    for key in ourDictionnary:
         ourDictionnary[key]['bikes'] = int(ourDictionnary[key]['bikes'] / amt_of_days)


    return ourDictionnary

