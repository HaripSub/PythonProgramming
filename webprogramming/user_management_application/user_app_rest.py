from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId  # For handling ObjectId in MongoDB

app = Flask(__name__)

# Connect to MongoDB (adjust the connection string as needed)
client = MongoClient( 'mongodb+srv://haripriyasubramanian:eMzz0qKkY15KfEfN@cluster0.2qhc3hk.mongodb.net/')
db = client['usersdb']  # Replace 'your_database_name' with your database name
users_collection = db['users']  # Collection name


# Route to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
    return jsonify(users)


# Route to get a specific user by id
@app.route('/api/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({'_id': ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404


# Route to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Missing data'}), 400

    new_user = {
        'username': data['username'],
        'email': data['email']
    }
    result = users_collection.insert_one(new_user)
    new_user['_id'] = str(result.inserted_id)  # Convert ObjectId to string for JSON serialization
    return jsonify(new_user), 201


# Route to update an existing user
@app.route('/api/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = users_collection.find_one({'_id': ObjectId(user_id)})
    if not user:
        return jsonify({'error': 'User not found'}), 404

    users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    updated_user = users_collection.find_one({'_id': ObjectId(user_id)})
    updated_user['_id'] = str(updated_user['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(updated_user)


# Route to delete a user
@app.route('/api/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
