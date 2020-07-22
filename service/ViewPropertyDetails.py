from data import Connection


def view_property_details(property_id):  # view property details
    statement = """SELECT * FROM Based_Property bp JOIN Owned_Property op ON op.OwnershipID = bp.OwnershipID WHERE bp.PropertyID = %s"""
    property_details = get_property_details(statement, property_id)
    return property_details


def get_property_details(statement, row_id):
    try:
        connect = Connection.Connection
        cursor = connect.cursor()
        cursor.execute(statement, (row_id,))
        record = cursor.fetchone()
        return record
    except Exception as error:
        print("Selection Error: ", error)
        return None
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")

