from project.db_connection import SqlConnection

connector = SqlConnection()


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


def get_user(user_id):
    cnx = connector.connect()
    cursor = cnx.cursor()
    get_person = ("SELECT * FROM user "
                  "WHERE  id = %s ")

    cursor.execute(get_person, user_id)
    result = cursor.fetchone()
    print(result)
    return result

def get_all_users():
    cnx = connector.connect()
    cursor = cnx.cursor()
    get_all = "SELECT * FROM user"
    cursor.execute(get_all)
    result = cursor.fetchall()
    print(result)
    return result
