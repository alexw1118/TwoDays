from data import Get
from model import BaseProperty


def display(property_id):  # view property details
    statement = """SELECT * FROM BaseProperty WHERE PropertyID = ?"""
    base_property = BaseProperty.BaseProperty(Get.read(statement=statement, row_id=property_id))
    return vars(base_property)
