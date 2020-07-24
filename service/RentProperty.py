from data import Put


def rent(value):
    statement = """UPDATE BaseProperty SET RentID = ? WHERE PropertyID = ?"""
    token = Put.update(statement=statement, value=value)
    return token
