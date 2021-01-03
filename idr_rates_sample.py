import requests
# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.0728176530441e-5,"date":"Wed, 16 Dec 2020 00:00:02 GMT","inverseRate":14138.636807208},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.8228176906325e-5,"date":"Wed, 16 Dec 2020 00:00:02 GMT","inverseRate":17173.81606518}}
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])