import populationData
import bikeData
import treeData
import json
from flask import Flask, Response


app = Flask(__name__)
ourDictionnary = {}

@app.route('/get_data')
def get_data():

    return Response(json.dumps(ourDictionnary),content_type= "application/json")



if __name__ == "__main__":
    
    ourDictionnary = populationData.getPopulationPerHood()
    bikeData.getBikeData(ourDictionnary)
    treeData.getTreeData(ourDictionnary)

    app.run(debug=True)
    pass