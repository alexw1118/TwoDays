from utils import common
from data import Post, Get


def sign_up(user):
    statement = """INSERT INTO UserAccount (UserID, FullName, Username, Password, Email, Phone, UserPrivilege, BankName, BankAccount, IdentityCardNumber, ProfileImage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    token = validate_user(user)
    value = user.user_id, user.fullname, user.username, user.password, user.email, user.phone, user.privilege, user.bank_name, user.bank_account, user.identity_card, user.image
    if token[0] is True:
        token = Post.create(statement=statement, value=value)
    return (token, "User Registered Successfully!") if token is True else (False, "Unable to Registered User!")


def validate_user(user):
    statement = """SELECT * FROM UserAccount WHERE Username = ?"""
    required_field = (user.user_id, user.fullname, user.username, user.password, user.email, user.phone, user.privilege)
    if common.isNone(required_field) is False:
        if Get.read(statement=statement, row_id=user.username) is None:
            if common.valid_email(user.email) is True:
                if user.bank_name is not None:
                    if user.bank_account is not None:
                        if common.valid_integer(user.bank_account):
                            return True, "success"
                        return False, "Data Type Not Match!"
                    return False, "Bank Account Not Filled!"
                return True, "success"
            return False, "Invalid Email!"
        return False, "Username Existed!"
    return False, "Required Field Not Filled!"
