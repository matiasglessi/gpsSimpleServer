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
    cnx = connector.cursor()
    cursor = cnx.cursor()
    add_person = ("INSERT INTO user "
                  "(username, email, password) "
                  "VALUES (%s, %s, %s)")
    save = connector.modify()
    try:
        session.commit()
    except IntegrityError as e:
        session.rollback()
        raise BDError(str(e.orig))