from flask.blueprints import Blueprint

GPS_ENDPOINT = Blueprint(
    'gps_endpoint', __name__, template_folder='templates')