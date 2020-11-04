from app import create_app
from flask import Flask


def test_create_app_deve_retornar_um_app_flask():
    assert isinstance(create_app(), Flask)


def test_login_deve_retornar_sucesso():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.get('/login')

    assert response.status_code == 200
