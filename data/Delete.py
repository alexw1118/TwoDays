from data import Connection


def delete(statement, row_id):
    try:
        connect = Connection.Connection
        cursor = connect.cursor()
        cursor.execute(statement, (row_id,))
        connect.commit()
        print("Deletion Successful!")
        return True
    except Exception as error:
        print("Deletion Error: ", error)
        return False
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")
