from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/login')
    def login():
        return render_template('login.html')

    return app
