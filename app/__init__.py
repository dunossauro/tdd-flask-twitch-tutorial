from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/login')
    def login():
        return ''

    return app
