from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb+srv://haripriyasubramanian:eMzz0qKkY15KfEfN@cluster0.2qhc3hk.mongodb.net/')
db = client['usersdb']
users_collection = db['users']


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    return render_template('users.html', users=users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_user = {
            'username': request.form['username'],
            'email': request.form['email'],
        }
        result = users_collection.insert_one(new_user)
        return redirect(url_for('get_users'))
    return render_template('add_user.html')


@app.route('/users/<string:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = users_collection.find_one({'_id': ObjectId(user_id)})
    if request.method == 'POST':
        updated_user = {
            'username': request.form['username'],
            'email': request.form['email'],
        }
        users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user})
        return redirect(url_for('get_users'))
    return render_template('edit_user.html', user=user)


@app.route('/users/delete/<string:user_id>', methods=['POST'])
def delete_user(user_id):
    users_collection.delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('get_users'))


if __name__ == '__main__':
    app.run(debug=True)
