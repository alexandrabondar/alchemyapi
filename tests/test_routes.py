import models
import pytest
from app import app
from distance import get_distance
from get_api_data import get_weather_yandex
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_check_list_cities(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200


def test_get_city(client):
    response = client.get('/api/v1/city/Minsk')
    mock_request_data = {
        "response": ["Minsk", "27.561831", "53.902284"]
    }
    assert response.status_code == 200
    assert response.json == mock_request_data


def test_get_weather(client):
    response = client.get('/api/v1/weather/city/Minsk/')
    data = get_weather_yandex('Minsk')
    mock_request_data = {
        "weather_city": data
    }
    assert response.status_code == 200
    assert response.json == mock_request_data


def test_get_distance(client):
    response = client.post('/api/v1/distance/cities/Minsk/Kiev/')
    data = get_distance('Minsk', 'Kiev')
    mock_request_data = {
        "distance": data
    }
    assert response.status_code == 200
    assert response.json == mock_request_data


@pytest.fixture(scope="session")
def connection():
    engine = create_engine(
        "postgresql://root:root@localhost:5432/about_city"
        )
    return engine.connect()


@pytest.fixture(scope="session")
def setup_database(connection):
    models.Base.metadata.bind = connection
    models.Base.metadata.create_all()
    yield
    models.Base.metadata.drop_all()


@pytest.fixture
def db_session(setup_database, connection):
    transaction = connection.begin()
    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    transaction.rollback()


def test_city_created(db_session):
    cities = [
        {
            "name_place_test": "Minsk",
            "lon_test": "27.561831",
            "lat_test": "53.902284"
        }
    ]
    for city in cities:
        db_city = models.CityTest(**city)
        db_session.add(db_city)
    db_session.commit()
