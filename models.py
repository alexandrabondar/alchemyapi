from config import db


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
