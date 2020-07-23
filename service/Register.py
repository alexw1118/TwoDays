from utils import common
from data import Post, Get


def sign_up(user):
    statement = """INSERT INTO UserAccount (UserID, FullName, Username, Password, Email, Phone, UserPrivilege, BankName, BankAccount, IdentityCardNumber, ProfileImage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    token = validate_user(user)
    if token[0] is True:
        return Post.create(statement=statement, value=user)
    return token


def validate_user(user):
    statement = """SELECT * FROM UserAccount WHERE Username = %s"""
    required_field = (user.user_id, user.fullname, user.username, user.password, user.email, user.phone, user.privilege)
    if common.isNone(required_field) is False:
        if Get.read(statement=statement, row_id=user.username) is None:
            if common.valid_email(user.email) is True:
                if user.bank_account is not None:
                    if common.valid_integer(user.bank_account):
                        return True, "success"
                    return False, "data type not match"
                return True, "success"
            return False, "invalid email"
        return False, "username existed"
    return False, "null"
