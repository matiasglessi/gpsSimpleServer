from flask import jsonify
from flask import request
from project.endpoints import verify_json
from project.service import user_service
from flask.blueprints import Blueprint

USER_ENDPOINT = Blueprint(
    'user_endpoint', __name__, template_folder='templates')


@USER_ENDPOINT.route('/user', methods=['POST'])
def save_user():
    json_data = request.json
    verify_json(
        json_data, ('user_id', 'username', 'password', 'email', 'first_name', 'last_name'))
    user_service.save_user(json_data['user_id'], json_data['username'], json_data['password'], json_data['email'], json_data['first_name'],
                           json_data['last_name'])
    return jsonify({"Succeed": True})


@USER_ENDPOINT.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    '''Returns a user by id'''
    user = user_service.get_user(user_id)

    return jsonify(user_id=user[0],
                   username=user[1],
                   email=user[3],
                   first_name=user[4],
                   last_name=user[5]
                   )


@USER_ENDPOINT.route('/user', methods=['GET'])
def get_all_users():
    '''Returns all users'''
    return jsonify(user_service.get_all_users())
