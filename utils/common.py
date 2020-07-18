from data import Connection


def verify(data):
    flag = False
    sql_statement = "select * from user"
    cur = Connection.Connection
    cur.execute(sql_statement)

    return flag


def validate(data):
    flag = False
    return flag


def isNone(data):
    return not all(data)  # True: contain null value, False: not contain null value

