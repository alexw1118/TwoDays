import re


def verify(input_data, existing_data):
    return True if input_data == existing_data else False  # True: correct credential, False: wrong credential


def valid_integer(data):
    value = int(data)
    if isinstance(value, int):
        return True
    return False          # True: is integer, False: not integer


def valid_decimal(data):
    value = float(data)
    if isinstance(value, float):
        return True
    return False          # True: is decimal, False: not decimal


def isNone(data):
    return not all(data)  # True: tuple contain null value, False: tuple not contain null value


def valid_email(data):
    regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return True if regex.match(data) else False  # True: email valid, False: email not valid
