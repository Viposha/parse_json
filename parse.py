import requests
import json

# download all packages api
response = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = response.json()

result = []
for package in packages_json[:5]:
    a = 0
    package_name = package['name']
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    response2 = requests.get(package_url)
    package_json = response2.json()
    a += 1
    package_dict = {
                'name': package_json['name'],
                'desc': package_json['desc'],
                'intalls_30d': package_json['analytics']['install']['30d'][package_name],
                'intalls_90d': package_json['analytics']['install']['90d'][package_name],
                'intalls_365d': package_json['analytics']['install']['365d'][package_name]
                    }
    result.append(package_dict)
    if a == 5:
        break
with open('install_info', 'w') as file:
    json.dump(result, file, indent=2)







