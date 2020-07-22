from data import Connection

#  after approved, when purchase button clicked, transaction start:
#  t1: signed contract & checkout to 3rd party payment api
#  t2: if payment success/ receive payment success token from 3rd party payment api, then insert payment into billing table
#  t3: execute transfer ownership


def pay_bill(value, billing_id):
    statement = """UPDATE Billing SET PaymentDate = %s WHERE BillingID = %s"""
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
