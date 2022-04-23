import requests
import json

response = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = response.json()

packages_name = packages_json[0]['name']
#print(packages_name)

big_data = json.dumps(packages_json[0], indent=2)



response2 = requests.get('https://formulae.brew.sh/api/formula/a2ps.json')
package_json = response2.json()

package_name = package_json['name']
package_desc = package_json['desc']
package_intalls_30d = package_json['analytics']['install']['30d']['a2ps']
package_intalls_90d = package_json['analytics']['install']['90d']['a2ps']
package_intalls_365d = package_json['analytics']['install']['365d']['a2ps']
#print(package_intalls_365d)
#print(package_json['name'])
one_package = json.dumps(package_json, indent=2)
#print(one_package)





