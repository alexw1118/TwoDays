from utils import common
from model import User
from data import Get


def sign_in(input_credential):
    statement = """SELECT * FROM UserAccount WHERE Username = ?"""
    user = User.User(Get.read(statement=statement, row_id=input_credential[0]))
    user_credential = user.username, user.password
    return (False, "null") if common.isNone(input_credential) \
        else (True, "success") if common.verify(input_credential, user_credential) \
        else (False, "fail")
