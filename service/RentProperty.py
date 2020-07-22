from data import Connection


def rent(value, property_id):
    statement = """UPDATE Base_Property SET RentID = %s WHERE PropertyID = %s"""
    token = update_property(statement, value, property_id)
    return token


def update_property(statement, value, row_id):
    try:
        connect = Connection.Connection
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
