import pandas as pd
import insert_data_csv_to_db as insert_data

def csv_to_json():
    df = pd.read_csv("penjat.csv")
    d = df.to_dict(orient='list')

    return d

data = csv_to_json()
#print(data["WORD"][102]) exemple
#print(data["THEME"][102]) exemple

for i in range(500):
    insert_data.insert_data_csv_to_db(i, data)