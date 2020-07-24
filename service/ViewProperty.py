from data import Get
from model import BaseProperty


def admin():  # admin view property
    statement = """SELECT * FROM BaseProperty WHERE IsDeleted = 0"""
    return view(statement=statement)


def sale():  # view for sale property list
    statement = """SELECT * FROM BaseProperty WHERE Usage = 'SALE' OR Usage = 'BOTH' OR OwnershipID = '7EE30661-80AD-4862-966B-7279D0F80D22'"""
    return view(statement=statement)


def rent():  # view for rent property list
    statement = """SELECT * FROM BaseProperty WHERE Usage = 'RENT' OR Usage = 'BOTH' AND RentID IS NULL"""
    return view(statement=statement)


def self(user_id):  # view own property list
    statement = """SELECT * FROM BaseProperty WHERE OwnershipID = ? OR RentID = ?"""
    property_list = []
    records = Get.read_multiple_with_2_param(statement=statement, row_id_1=user_id, row_id_2=user_id)
    for record in records:
        property_list.append(vars(BaseProperty.BaseProperty(record)))
    return property_list


def view(statement):
    property_list = []
    records = Get.read_all(statement=statement)
    for record in records:
        property_list.append(vars(BaseProperty.BaseProperty(record)))
    return property_list
