from flask import request, Blueprint
from assignments.a3.database.db import Database
import json

api = Blueprint('api', __name__)

db = Database()


@api.route('/api/data', methods=['GET', 'POST'])
def get_records():
    if request.method == 'POST':
        print(request.json)
        parameters = request.json
        print(parameters)
        last_id = db.add_record(parameters['category'], parameters['data1'], parameters['data2'])
        return {'id': last_id}, 200
    else:
        print(db.get_records())
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
