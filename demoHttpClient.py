import requests

klucz = ''# insert your own key to airly as string

url='https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
print ("code:"+ str(response.status_code))
print ("******************")
print ("headers:"+ str(response.headers))
#print ("******************")
#print ("content:"+ str(response.text))
print ("******************")
j = response.json()
print(j[0]) # pokauje pierwszy rekord
print ("******************")
print("userID: " + str(j[0]['userId'])) 

url='https://airapi.airly.eu/v2/measurements/installation?installationId=6532'
headers = {'Accept': 'application/json', 'apikey':klucz} 
r2 = requests.get(url, headers = headers)
j2 = r2.json()
print ("******************")
print(j2['current']['values']) # wybiera aktualne dane
daneAktualne = j2['current']['values']
daneStandardowe = j2['current']['standards']
print("*******************")
print (str(daneStandardowe))
print("*******************")
print(str(daneAktualne[1]['name']) + ": " + str(daneAktualne[1]['value']) + " " + str((daneAktualne[1]['value']/daneStandardowe[0]['limit'])*100) + "%") # wybiera aktualne dane
print("*******************")