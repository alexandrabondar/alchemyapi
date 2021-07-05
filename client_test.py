# # open new terminal for test
# import requests
#
#
# # {'response': None}
# res1 = requests.post('http://localhost:5000/api/v1/city/create/Azbaza')
# if res1.ok:
#     print(res1)
# else:
#     print(res1)
#
#
# # {'response': ['Piter', '30.315877', '59.939099']}
# res2 = requests.get('http://localhost:5000/api/v1/city/Piter')
# if res2.ok:
#     print(res2.json())
# else:
#     print(res2)
#
# # {'distance': 433746}
# res3 = requests.post('http://localhost:5000//api/v1/distance/cities/Minsk/Kiev')
# if res3.ok:
#     print(res3.json())
# else:
#     print(res3)
#
#
# # {"weather_city":25}
# res5 = requests.get('http://localhost:5000/api/v1/weather/city/Minsk')
# if res5.ok:
#     print(res5.json())
# else:
#     print(res5)
#
#
# # {'cities': [{'lat': '53.902284', 'lon': '27.561831', 'name_place': 'Minsk'},
# # {'lat': '53.894548', 'lon': '30.330654', 'name_place': 'Mogilev'},
# # {'lat': '52.094246', 'lon': '23.684568', 'name_place': 'Brest'},
# # {'lat': '59.939099', 'lon': '30.315877', 'name_place': 'Piter'},
# # {'lat': '55.75322', 'lon': '37.622513', 'name_place': 'Moscow'},
# # {'lat': '53.677839', 'lon': '23.829529', 'name_place': 'Grodno'},
# # {'lat': '50.450441', 'lon': '30.52355', 'name_place': 'Kiev'},
# # {'lat': '52.42416', 'lon': '31.014281', 'name_place': 'Gomel'},
# # {'lat': '48.707067', 'lon': '44.516975', 'name_place': 'Volgograd'},
# # {'lat': '55.184217', 'lon': '30.202878', 'name_place': 'Vitebsk'},
# # {'lat': '54.782635', 'lon': '32.045287', 'name_place': 'Smolensk'}]}
# res6 = requests.get('http://localhost:5000/api/v1')
# if res6.ok:
#     print(res6.json())
# else:
#     print(res6)
