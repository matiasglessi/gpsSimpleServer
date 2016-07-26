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
        json_data, ('username', 'password', 'email', 'first_name', 'last_name'))
    user_service.save_user(json_data['username'], json_data['password'], json_data['email'], json_data['first_name'],
                           json_data['last_name'])
    json = jsonify({"Succeed": True})
    return json
