import requests

API_KEY = '6c1de415-f785-4a6f-92ac-09191d250706'


def take_weather():
    headers = {'X-Yandex-API-Key': API_KEY}
    res = requests.get('https://api.weather.yandex.ru/v2/informers?lat=59.9386&lon=30.3141',
                       headers=headers)
    if res:
        return res.json()
    else:
        print('Response Failed')
