#api nbp kursy walut
import urllib.request
import json
f = urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
#print(type(f))
print(f.status)  # status HTTP
#print(f)
#print(f.read())
data = f.read()
data = json.loads(data)
print(data)
kursy = data[0]['rates']
#print(data[0]['rates'])
for kurs in kursy:
    print(f"{kurs['currency']} - {kurs['code']} - {kurs['mid']}")
#print(json.loads(data))
#print(dir(f))
# f = f.read()