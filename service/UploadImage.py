from data import Put


def upload(image, user_id):
    statement = """UPDATE UserAccount SET ProfileImage = %s WHERE UserID = %s"""
    token = Put.update(statement=statement, value=image, row_id=user_id)
    return token


def bulk_upload(images, property_id):
    statement = """UPDATE BaseProperty SET Images = %s WHERE PropertyID = %s"""
    token = Put.update(statement=statement, value=images, row_id=property_id)
    return token
