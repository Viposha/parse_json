import json
from collections import ChainMap

with open('install_info') as file:
    install_data = json.load(file)



general_data = []
for item in install_data:
    name = item['name']
    installs_365 = item['intalls_365d']
    installs = {
            name: installs_365
                }
    general_data.append(installs)
print(general_data)


myDict = dict(ChainMap(*general_data))


sorted_dict = {}
sorted_keys = sorted(myDict, key=myDict.get, reverse=True)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = myDict[w]

print(sorted_dict)