import requests
from flask import Flask, request
from flask import render_template
from database.api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


app = create_app()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.route('/')
def homepage():
    response = requests.get('http://127.0.0.1:5000/api/data').json()
    return render_template('index.html', result=response)


@app.route('/add', methods=['POST'])
def add():
    response = requests.post('http://127.0.0.1:5000/api/data', json={
        'category': request.form['category'],
        'data1': request.form['data1'],
        'data2': request.form['data2']
    })
    if response.status_code == 200:
        return homepage()
    elif response.status_code == 400:
        return render_template('errors/400.html', message=response.json()['message']), 400


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    response = requests.delete('http://127.0.0.1:5000/api/data/' + str(record_id))
    if response.status_code == 200:
        return homepage()
    elif response.status_code == 404:
        return render_template('errors/404.html', message=response.json(['message'])), 404


if __name__ == '__main__':
    app.run(debug=True)
