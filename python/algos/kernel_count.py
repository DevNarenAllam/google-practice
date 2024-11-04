data = {  
  "Pets":[  
    {  
      "Breed":"Dingo",
      "IsFixed":False,
      "Name":"Fido",
      "Source":"Australia Kennel Network",
      "Type":"Dog"
    },
    {  
      "Breed":"Siamese",
      "IsFixed":True,
      "Name":"Fluffy",
      "Source":"Lost and Found",
      "Type":"Cat"
    }
  ]
}

import sys
import json

jsonTxt = ''
for line in sys.stdin:
    jsonTxt += line
    
# data = json.loads(jsonTxt)

pets = data['Pets']
print(pets)
petsByType = {}
result = {}

for pet in pets:
    if pet not in petsByType:
        petsByType = [breed]
    else:
        petsByType.append(breed)


print(petsByType)