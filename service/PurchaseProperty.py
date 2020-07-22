from data import Connection


def purchase(value):
    statement = """INSERT INTO Owned_Property (RentPrice, SellPrice) VALUES (%s, %s)"""
    token = add_new_ownership(statement, value)
    return token


def transfer_ownership(value, property_id):
    statement = """UPDATE Owned_Property SET UserID = %s WHERE OwnershipID = %s"""
    token = update_owned_property(statement, value, property_id)
    return token


def add_new_ownership(statement, value):
    try:
        connect = Connection.Connection
        cursor = connect.cursor()
        cursor.execute(statement, value)
        connect.commit()
        print("Insertion Successful!")
        return True
    except Exception as error:
        print("Insertion Error: ", error)
        return False
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")


def update_owned_property(statement, value, row_id):
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
