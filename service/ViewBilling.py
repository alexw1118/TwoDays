from data import Connection


def view_my_billing(user_id):  # view billing list
    statement = """SELECT * FROM Billing b JOIN Base_Property bp ON bp.PropertyID = b.PropertyID INNER JOIN Owned_Property op ON op.OwnershipID = bp.OwnershipID WHERE bp.RentID = %s OR op.UserID = %s"""
    property_list = get_my_billing(statement, user_id)
    return property_list


def view_all_billing():  # admin view billing list
    statement = """SELECT * FROM Billing WHERE BillingType != 'Rental'"""
    property_list = get_all_billing(statement)
    return property_list


def get_all_billing(statement):
    try:
        connect = Connection.Connection
        cursor = connect.cursor()
        cursor.execute(statement)
        records = cursor.fetchall()
        return records
    except Exception as error:
        print("Selection Error: ", error)
        return None
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")


def get_my_billing(statement, row_id):
    try:
        connect = Connection.Connection
        cursor = connect.cursor()
        cursor.execute(statement, (row_id,))
        records = cursor.fetchall()
        return records
    except Exception as error:
        print("Selection Error: ", error)
        return None
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")
