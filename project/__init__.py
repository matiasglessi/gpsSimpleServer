from flask import Flask

app = Flask(__name__)

from project.endpoints.gps_endpoint import GPS_ENDPOINT
from project.endpoints.user_endpoint import USER_ENDPOINT

app.register_blueprint(USER_ENDPOINT)
app.register_blueprint(GPS_ENDPOINT)
