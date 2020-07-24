from data import Post, Put


def request(value):
    statement = """INSERT INTO Request (RequestDate, RequestStatus, RequestType, RentalStartDate, RentalPeriod, UserID, PropertyID) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    token = Post.create(statement=statement, value=value)
    return token


def response(value):
    statement = """UPDATE Request SET RequestStatus = ? WHERE RequestID = ?"""
    token = Put.update(statement=statement, value=value)
    return token
