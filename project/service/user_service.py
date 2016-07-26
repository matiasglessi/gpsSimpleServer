from project.entities import User
from project.dao import user_dao


def save_user(username, password, email, first_name, last_name, date_of_birth):
    '''Saves a user'''
    user = User(username, password, email, first_name, last_name, date_of_birth)
    user_dao.save_user(user)

