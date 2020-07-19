from data import Connection


def read_all(statement):
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


def read(statement, row_id):
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
