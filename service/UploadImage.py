from data import Connection


def upload_profile_image(value, user_id):
    statement = """UPDATE UserAccount SET ProfileImage = %s WHERE UserID = %s"""
    token = update_image(statement, value, user_id)
    return token


def upload_property_images(value, property_id):
    statement = """UPDATE BaseProperty SET Images = %s WHERE PropertyID = %s"""
    token = update_image(statement, value, property_id)
    return token


def update_image(statement, value, row_id):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        cursor.execute(statement, (value, row_id))
        connect.commit()
        print("Modification Successful!")
        return True
    except Exception as error:
        print("Modification Error: ", error)
        return False
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")
