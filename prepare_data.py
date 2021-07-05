from models import CityModel, db
from get_api_data import get_coords_yandex
from flask import abort

coords = {}
cities = []


def check_valid_data(city_name):
    tmp_list = []
    data_db = CityModel.query.all()
    for city in data_db:
        tmp_list.append(city.name_place)
    if city_name in tmp_list:
        return True
    else:
        return False


def get_data(city):
    if check_valid_data(city):
        city = CityModel.query.filter_by(name_place=city).first_or_404()
        response = (city.name_place, city.lon, city.lat)
        return response
    else:
        abort(404)


def insert_to_db(city):
    if not check_valid_data(city):
        city, lon, lat = get_coords_yandex(city)
        coords['name_place'] = city
        coords['lon'] = lon
        coords['lat'] = lat
        cities.append(coords)
        new_city = CityModel(name_place=coords['name_place'], lon=coords['lon'], lat=coords['lat'])
        db.session.add(new_city)
        db.session.commit()
        return city, lon, lat
    else:
        abort(400)


def get_list_cities():
    list_cities = CityModel.query.all()
    results = [
        {
            "name_place": city.name_place,
            "lon": city.lon,
            "lat": city.lat
        } for city in list_cities]
    return results


def prepare_data_distance(city):
    if check_valid_data(city):
        data = get_data(city)
        return data
    else:
        record_to_insert = insert_to_db(city)
        data = record_to_insert
        return data
