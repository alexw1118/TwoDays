from data import Connection


def update(value, property_id):
    statement = """UPDATE Owned_Property SET Furnish = %s, RentPrice = %s, SellPrice = %s, Usage = %s, Images = %s, RentalStartDate = %s, RentalEndDate = %s, RentalPeriod = %s, Description = %s, LastUpdatedDate = %s, Contract = %s WHERE Property_id = %s"""
    token = update_property_details(statement, value, property_id)
    return token


def update_property_details(statement, value, row_id):
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
