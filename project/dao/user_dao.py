from project.db_connection import SqlConnection

from project.entities import User
from project.exceptions import EntityNotFound, BDError

connector = SqlConnection()


def savePlayerDao(player):
    cursor = connector.connect()
    cursor = connector.cursor()

    cursor = cnx.cursor()

    add_person = ("INSERT INTO player "
                  "(username, email, password) "
                  "VALUES (%s, %s, %s)")

    data_player = (player.username, player.email, player.password)

    cursor.execute(add_person, data_player)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()


def save_user(user):
    cnx = connector.connect()
    cursor = cnx.cursor()
    add_person = ("INSERT INTO user "
                  "(username, pass, email, first_name, last_name) "
                  "VALUES (%s, %s, %s, %s, %s)")

    data = (user.username, user.password, user.email, user.first_name, user.last_name)
    cursor.execute(add_person, data)
    cnx.commit()
    cursor.close()
