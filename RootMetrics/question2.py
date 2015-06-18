# question 1

# dependencies
import os
import pandas as pd
import numpy as np
import json



# directory containing this file
filedir = os.path.dirname(os.path.realpath(__file__))

# select json output file
output_path = os.path.join(filedir, "json_dump.txt")



# import data
csv_path = os.path.join(filedir, "data.csv")
df = pd.read_csv(csv_path)

# get set of carriers names
carriers = set(df['Carrier'].tolist())

# create json data structure
datastruct = []
for carrier in carriers:
    
    # get carrier specific data from raw data
    df_carrier = df[df['Carrier']==carrier]
    
    # init empty carrier data structure
    carrier_ds = {
        "Carrier": carrier,
        "plots": []
    }
    
    # fill carrier structure
    for idx, row in df_carrier.iterrows():
        carrier_ds["plots"].append({
            "Activity": row["Activity"],
            "Data_Direction": row["Data_Direction"],
            "Final_Test_Speed": row["Final_Test_Speed"]
        })
        
    # save carrier data to structure
    datastruct.append(carrier_ds)
    

# write results to file as in json
with open(output_path, 'w') as outfile:    
    jsondump = json.dumps(datastruct, output_path, sort_keys=True, indent=4)
    outfile.write(jsondump)
    
