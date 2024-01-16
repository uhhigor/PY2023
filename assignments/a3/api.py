from flask import request, Blueprint
from assignments.a3.database.database import Database
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import json


api = Blueprint('api', __name__)
db = Database()


@api.route('/api/data', methods=['GET', 'POST'])
def get_records():
    if request.method == 'POST':
        parameters = request.json
        if not isinstance(parameters['category'], int):
            print(type(parameters['category']))
            return {'message': 'Invalid input: category must be an integer'}, 400
        if not isinstance(parameters['data1'], float):
            return {'message': 'Invalid input: data1 must be float'}, 400
        if not isinstance(parameters['data2'], float):
            return {'message': 'Invalid input: data2 must be float'}, 400
        last_id = db.add_record(parameters['category'], parameters['data1'], parameters['data2'])
        return {'id': last_id}, 200
    else:
        return json.dumps(db.get_records()), 200


@api.route('/api/data/<int:record_id>', methods=['GET', 'DELETE'])
def get_record(record_id):
    result = json.dumps(db.get_record(record_id))
    if result != '{}':
        if request.method == 'GET':
            return result, 200
        elif request.method == 'DELETE':
            last_id = db.delete_record(record_id)
            return {'id': last_id}, 200
    else:
        return {'message': 'Record not found'}, 404


@api.route('/api/predictions', methods=['GET', 'POST'])
def predict_category():
    if request.method == 'POST':
        parameters = request.json
        print(parameters)
        if not isinstance(parameters['data1'], float):
            return {'message': 'Invalid input: data1 must be float'}, 400
        if not isinstance(parameters['data2'], float):
            return {'message': 'Invalid input: data2 must be float'}, 400

        data = db.get_records()
        features = [[item['data1'], item['data2']] for item in data]
        labels = [item['category'] for item in data]

        scaler = StandardScaler()
        features_standardized = scaler.fit_transform(features)

        knn_classifier = KNeighborsClassifier()
        knn_classifier.fit(features_standardized, labels)

        input_data_standardized = scaler.transform([[parameters['data1'], parameters['data2']]])

        prediction_result = knn_classifier.predict(input_data_standardized)

        return {'message': int(prediction_result)}, 200
