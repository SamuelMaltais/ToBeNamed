import populationData
import bikeData
import treeData

from flask import Flask, Response


app = Flask(__name__)

@app.route('/get_data')
def get_data():
    json_data = read_csv_to_json(csv_file_path) 
    print(json.dumps(json_data))
    
    return Response(json.dumps(json_data),content_type= "application/json")





if __name__ == "__main__":


    ourDictionnary = populationData.getPopulationPerHood()
    bikeData.getBikeData(ourDictionnary)
    treeData.getTreeData(ourDictionnary)


    pass