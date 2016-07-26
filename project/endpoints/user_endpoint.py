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
        json_data, ('username', 'pass', 'email', 'first_name', 'last_name', 'date_of_birth'))
    user_service.save_user(json_data['username'], json_data['pass'], json_data['email'], json_data['first_name'],
                           json_data['last_name'],
                           json_data['date_of_birth'])
    json = jsonify({"Succeed": True})
    return json
