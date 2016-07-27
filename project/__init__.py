from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

from project.endpoints.gps_endpoint import GPS_ENDPOINT
from project.endpoints.user_endpoint import USER_ENDPOINT

app.register_blueprint(USER_ENDPOINT)
app.register_blueprint(GPS_ENDPOINT)