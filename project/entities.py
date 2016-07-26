class User:
    def __init__(self, username, password, email, first_name, last_name, date_of_birth):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


class Gps:
    def __init__(self, user_id, longitude, latitude, time):
        self.user_id = user_id
        self.longitude = longitude
        self.latitude = latitude
        self.time = time
