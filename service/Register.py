from utils import common
from data import Connection
from service import Login


def register(user):
    token = validate_user(user)
    if token[0] is True:
        return create_user(user)
    return token


def validate_user(user):
    required_field = (user.fullname, user.username, user.password, user.email, user.phone, user.privilege)
    if common.isNone(required_field) is False:
        if Login.get_user_details(user.username) is not None:
            if common.valid_email(user.email) is True:
                if user.bank_account is not None:
                    if common.valid_integer(user.bank_account):
                        return True, "success"
                    return False, "data type not match"
                return True, "success"
            return False, "invalid email"
        return False, "username existed"
    return False, "null"


def create_user(value):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        statement = """INSERT INTO UserAccount (FullName, Username, Password, Email, Phone, UserPrivilege, BankName, BankAccount, IdentityCardNumber, ProfileImage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(statement, value)
        connect.commit()
        print("Insertion Successful!")
        return True
    except Exception as error:
        print("Insertion Error: ", error)
        return False
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")
