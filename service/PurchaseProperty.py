from data import Connection


def purchase(value):
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township, Contract, ContactPeriod, RentID, OwnershipID, RentPrice, SellPrice, Images, RentalStartDate, RentalEndDate, RentalPeriod, Description, LastUpdatedDate, RentContract, SellContract) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    token = add_new_ownership(statement, value)
    return token
#

def transfer_ownership(value, is_deleted, property_id, ownership_id):
    statement = """UPDATE BaseProperty SET IsDeleted = %s WHERE PropertyUID = %s AND OwnershipID = %s"""
    token = update_previous_property(statement, is_deleted, property_id, ownership_id)
    if token is True:
        token = purchase(value)
    return token


def add_new_ownership(statement, value):
    try:
        connect = Connection.connection()
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


def update_previous_property(statement, value, row_id_1, row_id_2):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        cursor.execute(statement, (value, row_id_1, row_id_2))
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
