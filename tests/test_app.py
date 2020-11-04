from app import create_app
from flask import Flask, template_rendered


def test_create_app_deve_retornar_um_app_flask():
    assert isinstance(create_app(), Flask)


def test_login_deve_retornar_sucesso():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.get('/login')

    assert response.status_code == 200


def test_endpoint_de_login_deve_retornar_o_template_de_login():
    app = create_app()
    app.config['TESTING'] = True

    templates = []

    def gravador_de_templates(remetente, template, context, **extra):
        templates.append(template)

    template_rendered.connect(gravador_de_templates, app)

    with app.test_client() as client:
        client.get('/login')

    assert templates[0].name == 'login.html'

    template_rendered.disconnect(gravador_de_templates, app)
    
