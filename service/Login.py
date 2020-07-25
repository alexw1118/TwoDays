from utils import common
from model import User
from data import Get, Connection


def sign_in(input_credential):
    statement = """SELECT * FROM UserAccount WHERE Username = ?"""
    user = User.User(Get.read(statement=statement, row_id=input_credential[0]))
    user_credential = user.username, user.password
    return (False, "null") if common.isNone(input_credential) \
        else (True, "success") if common.verify(input_credential, user_credential) \
        else (False, "fail")


def user_detail(username):  # view billing list
    statement = """SELECT * FROM UserAccount WHERE username = ?"""
    return view(statement, username)


def view(statement, row_id):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        cursor.execute(statement, (row_id,))
        records = cursor.fetchall()
        return records
    except Exception as error:
        print("Selection Error: ", error)
        return None
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")
