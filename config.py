from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/city_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api_key_coords = '554460af-543f-4ea4-ad52-9ff6b81d1d41'
api_key_weather = '0a9a5a24-926c-45af-b3ca-5299817a0333'
api_uri_coords = '1.x/?format=json&apikey='
api_uri_weather = 'v2/forecast?lat='
