from flask import request, jsonify
from get_api_data import get_weather_yandex
from prepare_data import insert_to_db, get_data, get_list_cities
from distance import get_distance
from config import app


@app.route('/api/v1/city/<name_place>', methods=['GET'])
def get_city(name_place):
    if request.method == 'GET':
        response = get_data(name_place)
        return jsonify({'response': response}), 200
    else:
        return app.register_error_handler(404)


@app.route('/api/v1/city/create/<name_place>', methods=['POST'])
def create_query_city(name_place):
    if request.method == 'POST':
        data = insert_to_db(name_place)
        return jsonify({'response': data}), 200
    else:
        return app.register_error_handler(404)


@app.route('/api/v1/distance/cities/<string:name_place1>/<string:name_place2>/', methods=['POST'])
def distance_city(name_place1, name_place2):
    if name_place1 and name_place2:
        distance = get_distance(name_place1, name_place2)
        return jsonify({'distance': distance}), 200
    else:
        return app.register_error_handler(404)


@app.route('/api/v1/weather/city/<string:name_place>/', methods=['GET'])
def weather_city(name_place):
    if name_place:
        weather = get_weather_yandex(name_place)
        return jsonify({'weather_city': weather}), 200
    else:
        return app.register_error_handler(404)


@app.route('/api/v1/', methods=['GET'])
def check_list_cities():
    if request.method == 'GET':
        list_cities = get_list_cities()
        return jsonify({'cities': list_cities}), 200
    else:
        return app.register_error_handler(404)


if __name__ == '__main__':
    app.run(debug=True)
