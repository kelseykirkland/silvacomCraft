import pytest
import json
from main import app

def test_root():
    response = app.test_client().get('/api/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello World'

def test_route_fail():
    response = app.test_client().get('/api/notexist')
    assert response.status_code == 404

def test_getCities():
    response = app.test_client().get('/api/cities')
    res = json.loads(response.data.decode('utf-8')).get("Cities")
    assert response.status_code == 200
    assert type(res) is list
    assert len(res) == 5
    assert res[0]['label'] == 'Venice'
    assert res[1]['label'] == 'Innsbruck'

def test_getWeather_Munich():
    response = app.test_client().get('/api/weather/Munich')
    res = json.loads(response.data.decode('utf-8')).get("location")
    assert response.status_code == 200
    assert res['name'] == 'Munich'
    assert res['country'] == 'Germany'

def test_getWeather_Venice():
    response = app.test_client().get('/api/weather/Venice')
    res = json.loads(response.data.decode('utf-8')).get("location")
    assert response.status_code == 200
    assert res['name'] == 'Venice'
    assert res['country'] == 'Italy'

def test_getWeather_NoParams():
    response = app.test_client().get('/api/weather/')
    assert response.status_code == 404

def test_getWeather_incorrectCity():
    response = app.test_client().get('/api/weather/NotExist')
    assert response.status_code == 500