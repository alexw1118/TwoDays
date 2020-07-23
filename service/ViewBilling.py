from data import Get
from model import Billing


def check(user_id):  # view billing list
    statement = """SELECT * FROM Billing b JOIN BaseProperty bp ON bp.PropertyID = b.PropertyID WHERE bp.RentID = %s OR bp.OwnershipID = %s"""
    billing_list = []
    records = Get.read_multiple(statement=statement, row_id=user_id)
    for record in records:
        billing_list.append(vars(Billing.Billing(record)))
    return billing_list


def admin():  # admin view billing list
    statement = """SELECT * FROM Billing WHERE BillingType != 'Rental'"""
    billing_list = []
    records = Get.read_multiple(statement=statement)
    for record in records:
        billing_list.append(vars(Billing.Billing(record)))
    return billing_list
