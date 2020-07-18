from utils import common


def login(username, password):
    user_data = username, password
    if common.isNone(user_data):
        message = "null value is not allowed!"
    else:
        message = "verification success!" if common.verify(user_data) else "failed to verify!"
    return message

