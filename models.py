from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


class CityModel(db.Model):
    __tablename__ = 'cities'

    id_place = db.Column(db.Integer, primary_key=True)
    name_place = db.Column(db.String())
    lon = db.Column(db.String())
    lat = db.Column(db.String())

    def __init__(self, name_place, lon, lat):
        self.name_place = name_place
        self.lon = lon
        self.lat = lat

    def __repr__(self):
        return f'Place {self.name_place}'


Base = declarative_base()


class CityTest(Base):
    __tablename__ = "cities_test"

    id_test = Column(Integer, primary_key=True)
    name_place_test = Column(String())
    lon_test = Column(String())
    lat_test = Column(String())
