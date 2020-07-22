from data import Connection


def view_property_details(property_id):  # view property details
    statement = """SELECT * FROM BaseProperty WHERE PropertyID = %s"""
    property_details = get_property_details(statement, property_id)
    return property_details


def get_property_details(statement, row_id):
    try:
        connect = Connection.connection()
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
