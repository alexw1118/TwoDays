from data import Connection


def request(value):
    statement = """INSERT INTO Request (RequestDate, RequestStatus, RequestType, UserID, PropertyID) VALUES (%s, %s, %s, %s, %s)"""
    token = create_request(statement, value)
    return token


def response(value, request_id):
    statement = """UPDATE Request SET RequestStatus = %s WHERE RequestID = %s"""
    token = response_request(statement, value, request_id)
    return token


def create_request(statement, value):
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


def response_request(statement, value, row_id):
    try:
        connect = Connection.Connection
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
