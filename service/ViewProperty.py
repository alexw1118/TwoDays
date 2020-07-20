from data import Connection


def view_all_property():  # user view list
    statement = """SELECT * FROM Based_Property"""
    property_list = get_all_property(statement)
    return property_list


def view_all_for_sell_property():  # view for sell property list
    statement = """SELECT * FROM Based_Property WHERE OwnershipID = null OR Usage = 'SELL'"""
    property_list = get_all_property(statement)
    return property_list


def view_all_for_rent_property():  # view for rent property list
    statement = """SELECT * FROM Based_Property bp INNER JOIN Owned_Property op ON op.OwnershipID = bp.OwnershipID WHERE bp.OwnershipID != null AND op.Usage = 'BOTH' OR op.Usage = 'RENT'"""
    property_list = get_all_property(statement)
    return property_list


def view_my_property(user_id):  # view own property list
    statement = """SELECT * FROM Based_Property bp INNER JOIN Owned_Property op ON op.OwnershipID = bp.OwnershipID WHERE op.UserID = %s OR bp.RentID = %s"""
    property_list = get_all_owned_property(statement, user_id)
    return property_list


def get_all_property(statement):
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


def get_all_owned_property(statement, row_id):
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
