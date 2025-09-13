from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello_default():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_hello_with_name():
    response = client.get("/hello?name=Minato")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Minato!"}
