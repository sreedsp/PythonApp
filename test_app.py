# test_app.py

import pytest # type: ignore
from app import create_app
from urllib.parse import quote

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = 'This is a new version'
    print(response.data)
    assert expected_text.encode() == response.data
