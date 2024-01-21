import populationData
import bikeData
import treeData
import evCarsData
import airPollution
from flask_cors import CORS, cross_origin
import json
from flask import Flask, Response


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ourDictionnary = {}

@app.route('/get_data')
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
        return Response(json.dumps(data),content_type= "application/json")

@app.route('/get_data_test')
def get_data_test():
    return Response(json.dumps(ourDictionnary),content_type= "application/json")

def createData():
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
    with open('data.json', 'w') as f:
        json.dump(ourDictionnary, f)

    return ourDictionnary

createData()

if __name__ == "__main__":

    print("Now listening on port 5000")
    

    app.run()