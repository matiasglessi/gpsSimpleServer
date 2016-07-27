from project import db
import sqlalchemy as sa


class User(db.Model):

    '''This class represents a user'''
    user_id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(255), unique=True)
    password = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255), unique=True)
    first_name = sa.Column(sa.String(255))
    last_name = sa.Column(sa.String(255))
    gps = relationship('gpsPoint', backref='owner', lazy='dynamic')


    def __init__(self, user_id, username, password, email, first_name, last_name):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


class Gps(db.Model):

    '''This class represents a gps point'''
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.user_id'))
    gps = sa.Column(sa.String(255), unique=True)
    latitude = sa.Column(sa.Decimal(9,6))
    longitude = sa.Column(sa.Decimal(9,6))
    gps_time = sa.Column(sa.DateTime(9,6))
    user = relationship("User")

    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name


    def __init__(self, user_id, longitude, latitude, time):
        self.user_id = user_id
        self.longitude = longitude
        self.latitude = latitude
        self.time = time


