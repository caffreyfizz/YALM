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
toponym = json_response["response"]["GeoObjectCollection"][
    'metaDataProperty']['GeocoderResponseMetaData']['boundedBy']['Envelope']

toponym_coodrinates = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta1 = str(abs(float(toponym['lowerCorner'].split()[0]) - float(toponym['lowerCorner'].split()[1])))
delta2 = str(abs(float(toponym['upperCorner'].split()[0]) - float(toponym['upperCorner'].split()[1])))

map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": get_spn(toponym),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()