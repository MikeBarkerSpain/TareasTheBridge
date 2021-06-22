import json
import pandas as pd 

from pandas.core.frame import DataFrame

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

def create_df ():
    return pd.DataFrame(data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]})