from data import Get
from model import BaseProperty


def show_historical_price(property_uid):
    statement = """SELECT * FROM BaseProperty WHERE PropertyUID = ?"""
    property_list = []
    records = Get.read_multiple(statement=statement, row_id=property_uid)
    for record in records:
        property_list.append(vars(BaseProperty.BaseProperty(record)))
    return property_list
