from data import Put


def rent(user_id, property_id):
    statement = """UPDATE BaseProperty SET RentID = ? WHERE PropertyID = ?"""
    token = Put.update(statement=statement, value=user_id, row_id=property_id)
    return token
