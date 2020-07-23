from data import Post, Put


def request(value):
    statement = """INSERT INTO Request (RequestDate, RequestStatus, RequestType, UserID, PropertyID) VALUES (%s, %s, %s, %s, %s)"""
    token = Post.create(statement=statement, value=value)
    return token


def response(request_status, request_id):
    statement = """UPDATE Request SET RequestStatus = %s WHERE RequestID = %s"""
    token = Put.update(statement=statement, value=request_status, row_id=request_id)
    return token
