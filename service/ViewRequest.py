from data import Connection


def view_pending_request():  # admin view pending request list
    statement = """SELECT * FROM Request r JOIN BaseProperty bp ON bp.PropertyID = r.PropertyID WHERE bp.OwnershipID = bp.PropertyUID"""
    property_list = get_all_request(statement)
    return property_list


def view_pending_request(user_id):
    statement = """SELECT * FROM Request r JOIN BaseProperty bp ON bp.PropertyID = r.PropertyID WHERE op.UserID = %s"""
    property_list = get_my_request(statement, user_id)
    return property_list


def get_all_request(statement):
    try:
        connect = Connection.connection()
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


def get_my_request(statement, row_id):
    try:
        connect = Connection.connection()
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
