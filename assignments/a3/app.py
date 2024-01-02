import requests
from flask import Flask
from flask import render_template
from database.api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


app = create_app()


@app.route('/')
def homepage():
    data = requests.get('http://127.0.0.1:5000/api/data').json()
    return render_template('index.html', result=data)


if __name__ == '__main__':
    app.run(debug=True)
