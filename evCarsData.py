import json
import requests
import os

def getEvCarsData(ourDictionnary):
    print("Starting the collection of Car collection Data !")
    
    path = "Data" + os.path.sep + "Vehicule_En_Circulation_2022.csv"
    with open(path) as topo_file:
        for line in topo_file:
            print(line)
                        
    return ourDictionnary


getEvCarsData({})