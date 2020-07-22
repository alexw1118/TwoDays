from data import Connection


def pay_bill(value, billing_id):
    statement = """"""
    token = update_billing(statement, value, billing_id)
    return token


def update_billing(statement, value, row_id):
    try:
        connect = Connection.connection()
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
