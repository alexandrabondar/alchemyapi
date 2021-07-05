import requests
from config import api_key_coords, api_key_weather, api_uri_weather, api_uri_coords
from flask import abort


def get_coords_yandex(place):
    print(f'Get info from yandex api about city {place}')
    req = 'https://geocode-maps.yandex.ru/' + api_uri_coords + api_key_coords + '&geocode=' + place
    result = requests.get(req)
    found_city = result.json()['response']['GeoObjectCollection']['featureMember']
    try:
        most_relevant = found_city[0]
    except IndexError:
        return abort(400)
    else:
        lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
        return place, lon, lat


def get_weather_yandex(place):
    print(f'Get info from yandex api about weather in {place}')
    city, lon, lat = get_coords_yandex(place)
    url = 'https://api.weather.yandex.ru/' + api_uri_weather + lat + '&lon=' + lon
    headers = {'X-Yandex-API-Key': api_key_weather}
    result = requests.get(url, headers=headers)
    avg_temp = result.json()['forecasts'][0]['parts']['day']['temp_avg']
    return avg_temp
