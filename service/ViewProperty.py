from data import Get
from model import BaseProperty


def sale():  # view for sale property list
    statement = """SELECT * FROM BaseProperty WHERE OwnershipID = null OR Usage = 'SALE' OR Usage = 'BOTH'"""
    return view(statement=statement)


def rent():  # view for rent property list
    statement = """SELECT * FROM BaseProperty WHERE OwnershipID != null AND Usage = 'BOTH' OR Usage = 'RENT'"""
    return view(statement=statement)


def self(user_id):  # view own property list
    statement = """SELECT * FROM BaseProperty WHERE OwnershipID = ? OR RentID = ?"""
    property_list = []
    records = Get.read_multiple(statement=statement, row_id=user_id)
    for record in records:
        property_list.append(vars(BaseProperty.BaseProperty(record)))
    return property_list


def view(statement):
    property_list = []
    records = Get.read_all(statement=statement)
    for record in records:
        property_list.append(vars(BaseProperty.BaseProperty(record)))
    return property_list
