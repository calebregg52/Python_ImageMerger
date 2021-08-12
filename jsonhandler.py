import json
import random

with open('sprites_data.json', 'r') as data_file:    
    data = json.load(data_file)
data_file.close()

for d in data["Backgrounds"]:
    print (d(['background_name']['odds'])