import requests
from flask import Flask, request
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


@app.route('/add', methods=['POST'])
def add():
    data = requests.post('http://127.0.0.1:5000/api/data', json={
        'category': request.form['category'],
        'data1': request.form['data1'],
        'data2': request.form['data2']
    }).json()
    return data


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    data = requests.delete('http://127.0.0.1:5000/api/data/' + str(record_id)).json()
    return data


if __name__ == '__main__':
    app.run(debug=True)
