from data import Get
from model import Request


def admin():  # admin view pending request list
    statement = """SELECT * FROM Request r INNER JOIN BaseProperty bp ON bp.PropertyID = r.PropertyID WHERE bp.OwnershipID = bp.PropertyUID"""
    request_list = []
    records = Get.read_all(statement=statement)
    for record in records:
        request_list.append(vars(Request.Request(record)))
    return request_list


def owner(user_id):
    statement = """SELECT * FROM Request r INNER JOIN BaseProperty bp ON bp.PropertyID = r.PropertyID WHERE bp.OwnershipID = %s"""
    request_list = []
    records = Get.read_multiple(statement=statement, row_id=user_id)
    for record in records:
        request_list.append(vars(Request.Request(record)))
    return request_list
