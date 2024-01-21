import pandas as pd 
from pathlib import Path 
import json
import os



def getPopulationPerHood(ourDictionnary):

    path = "Data" + os.path.sep + "population-quartiers-anciens-territoires-administratifs (1).csv"
    skip = 0
    with open(path) as topo_file:
        for line in topo_file:
            if skip < 5:
                skip += 1
            else:
                arr = line.split(",")
                quartier = arr[0].replace('"', ' ')

                quartier = quartier.replace("Ã©", "é")
                quartier = quartier.replace("Ã´", "ô")
                quartier = quartier.replace("Ã¨", "è")
                quartier = quartier.replace(" ", "")
                quartier = quartier.replace("ÃŽ", "î")

                if quartier == "Mercier":
                    quartier = "Mercier - Hochelaga-Maisonneuve"
                if quartier == "Notre-Dame-de-GrÃ¢ce":
                    quartier = "Côte-des-Neiges - Notre-Dame-de-Grâce"
                if quartier == "Vileray":
                    quartier = "Villeray—Saint-Michel—Parc-Extension"
                if quartier == "Rivière-des-Prairies":
                    quartier = "Rivière-des-Prairies - Pointe-aux-Trembles"

                arr[2] = arr[2].replace("\n", "")
                if(arr[2] == ""):
                    break

                if quartier in ourDictionnary:
                    if "population" in ourDictionnary:
                        ourDictionnary[quartier]['population'] += int(arr[2])
                    else:
                        ourDictionnary[quartier]['population'] = int(arr[2])
                else:
                    ourDictionnary[quartier] = {'population' : int(arr[2])}
                        
    return ourDictionnary









