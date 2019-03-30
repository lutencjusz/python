import json
data = {"jsonKey": "jsonValue","title": "hello world"}
print (json.dumps(data, indent=4, separators=(". ", " = ")))

with open('C:\Data\python\Demo_i_kurs\python\parametryCz.json') as jsonData:
    d = json.load(jsonData)
    print("VcMin: "+str(d["VcMin"]))
