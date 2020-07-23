from data import Get
from model import BaseProperty


def all_list():  # user view list
    statement = """SELECT * FROM BaseProperty"""
    return view(statement=statement)


def sell():  # view for sell property list
    statement = """SELECT * FROM BaseProperty bp WHERE bp.OwnershipID = null OR op.Usage = 'SELL' OR op.Usage = 'BOTH'"""
    return view(statement=statement)


def rent():  # view for rent property list
    statement = """SELECT * FROM BaseProperty WHERE OwnershipID != null AND Usage = 'BOTH' OR Usage = 'RENT'"""
    return view(statement=statement)


def self(user_id):  # view own property list
    statement = """SELECT * FROM BaseProperty WHERE OwnershipID = %s OR RentID = %s"""
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
