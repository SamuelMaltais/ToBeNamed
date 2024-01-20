import pandas as pd 
from pathlib import Path 
import json
import os

path = Path(r"C:\Users\rihaz\Dropbox\PC\Downloads\population-quartiers-anciens-territoires-administratifs.csv")

# TODO This should return an object
#
#"neighborhood-name" : {
#     "population": num,
# }
#
#
#
#
def getPopulationPerHood():
    pass

def read_csv_to_json(csv_file_path):
    
    df_file = pd.read_csv(path)
    df_file = df_file.drop(df_file.columns[[1]],axis =1)
    df_file = df_file.drop([df_file.index[0],df_file.index[3],df_file.index[2],df_file.index[67],df_file.index[68],df_file.index[69],df_file.index[70]])
    df_file = df_file.rename({'Unnamed: 0':'Quartiers de MONTRÉAL'},axis=1)
    print(df_file)
    json_data = df_file.to_json(orient="records")
    
    return json_data


if __name__ == "__main__":
    sdas
    pass




