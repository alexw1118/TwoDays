from data import Put


def rent(user_id, property_id):
    statement = """UPDATE Base_Property SET RentID = %s WHERE PropertyID = %s"""
    token = Put.update(statement=statement, value=user_id, row_id=property_id)
    return token
