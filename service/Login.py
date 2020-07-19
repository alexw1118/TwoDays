from utils import common
from model import User
from data import Connection


def login(input_credential):
    user = get_user_details(input_credential[0])
    user_credential = user.username, user.password
    return False, "null" if common.isNone(input_credential) \
        else True, "success" if common.verify(input_credential, user_credential) \
        else False, "fail"


def get_user_details(unique_row_key):
    try:
        connect = Connection.Connection
        cursor = connect.cursor()
        statement = """SELECT * FROM UserAccount WHERE Username = %s"""
        cursor.execute(statement, (unique_row_key,))
        record = cursor.fetchone()
        return User.User(record)
    except Exception as error:
        print("Selection Error: ", error)
        return None
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")