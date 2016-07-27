from project.entities import User
from project.dao import user_dao


def save_user(user_id, username, password, email, first_name, last_name):
    '''Saves a user'''
    user = User(user_id, username, password, email, first_name, last_name)
    user_dao.save_user(user)


def get_user(user_id):
    user = user_dao.get_user(user_id)
    return user


def get_all_users():
    users_list = user_dao.get_all_users()
    result = []
    for elem in users_list:
        map = {'username': elem.username, 'email': elem.email,
               'first_name': elem.first_name, 'last_name': elem.last_name}
        result.append(map)
    if result == []:
        result = {}
    return result
