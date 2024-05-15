from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['intellisqr']
collection = db['employees']

# CRUD operations

# Read operation
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = list(collection.find())
    # Convert ObjectId to string
    for employee in employees:
        employee['_id'] = str(employee['_id'])
    return jsonify({'employees': employees})

# Create operation
@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.json
    result = collection.insert_one(new_employee)
    return jsonify({'message': 'Employee created successfully', 'id': str(result.inserted_id)}), 201

# Update operation
@app.route('/employees/<string:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    query = {'_id': ObjectId(employee_id)}
    updated_employee = request.json
    result = collection.update_one(query, {'$set': updated_employee})
    if result.modified_count > 0:
        return jsonify({'message': 'Employee updated successfully'})
    else:
        return jsonify({'message': 'Employee not found'}), 404

# Delete operation
@app.route('/employees/<string:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    query = {'_id': ObjectId(employee_id)}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return jsonify({'message': 'Employee deleted successfully'})
    else:
        return jsonify({'message': 'Employee not found'}), 404

@app.route('/employees/<string:employee_id>', methods=['GET'])
def get_employee(employee_id):
    query = {'_id': ObjectId(employee_id)}
    employee = collection.find_one(query)
    if employee:
        # Convert ObjectId to string
        employee['_id'] = str(employee['_id'])
        return jsonify({'employee': employee})
    else:
        return jsonify({'message': 'Employee not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)
