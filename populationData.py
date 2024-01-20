import pandas as pd 
from pathlib import Path 
import json
from flask import Flask, Response


app = Flask(__name__)

path = Path(r"C:\Users\rihaz\Dropbox\PC\Downloads\population-quartiers-anciens-territoires-administratifs.csv")

def read_csv_to_json(csv_file_path):
    
    df_file = pd.read_csv(path)
    df_file = df_file.drop(df_file.columns[[1]],axis =1)
    df_file = df_file.drop([df_file.index[0],df_file.index[3],df_file.index[2],df_file.index[67],df_file.index[68],df_file.index[69],df_file.index[70]])
    df_file = df_file.rename({'Unnamed: 0':'Quartiers de MONTRÉAL'},axis=1)
    print(df_file)
    json_data = df_file.to_json(orient="records")
    
    return json_data

@app.route('/get_data')

def get_data():
    csv_file_path = r"C:\Users\rihaz\Dropbox\PC\Downloads\population-quartiers-anciens-territoires-administratifs.csv"
    json_data = read_csv_to_json(csv_file_path) 
    print(json.dumps(json_data))
    
    return Response(json.dumps(json_data),content_type= "application/json")

if __name__ == "__main__":
    app.run(debug=True)




