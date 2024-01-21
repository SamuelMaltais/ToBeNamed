import populationData
import bikeData
import treeData
import evCarsData
import airPollution

import json
from flask import Flask, Response


app = Flask(__name__)
ourDictionnary = {}

@app.route('/get_data')
def get_data():
    return Response(json.dumps(ourDictionnary),content_type= "application/json")

@app.route("/run")
def run():
    ourDictionnary = {}
    bikeData.getBikeData(ourDictionnary)
    print("Done with bikes")
    treeData.getTreeData(ourDictionnary)
    print("Done with trees")
    populationData.getPopulationPerHood(ourDictionnary)
    print("Done with population")
    airPollution.getAirPollution(ourDictionnary)
    print("Done with air pollution")
    #evCarsData.getEvCarsData(ourDictionnary)
    print("Done with Ev Cars Data")
    return Response(json.dumps(ourDictionnary),content_type= "application/json")


if __name__ == "__main__":
    print("Now listening on port 5000")
    app.run()