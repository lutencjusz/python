import json
data = {"jsonKey": "jsonValue","title": "hello world"}
print (json.dumps(data, indent=4, separators=(". ", " = ")))

with open('Demo/ustawieniaZ.json') as jsonData:
    d = json.load(jsonData)
    print("klucz: "+d["ssid"])
