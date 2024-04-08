import sys
from io import BytesIO
from test import get_spn

import requests
from PIL import Image
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.

toponym_coodrinates = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": f"{toponym_longitude},{toponym_lattitude}",
    "format": "json"}

adress = f"https://geocode-maps.yandex.ru/1.x"
if not adress:
    pass
response = requests.get(adress, params=params).json()
address_name = response["response"]["GeoObjectCollection"]["featureMember"][2][
'GeoObject']['metaDataProperty']['GeocoderMetaData']["Address"]['Components'][4]["name"]
print(address_name)