from data import Connection


def new_bill(value):
    statement = """"""
    token = add_billing(statement, value)
    return token


def add_billing(statement, value):
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
