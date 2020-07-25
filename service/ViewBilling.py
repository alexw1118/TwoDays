from data import Get
from model import Billing


def user(property_id):  # view billing list
    statement = """SELECT * FROM Billing WHERE PropertyID = ?"""
    return view(statement, property_id)


def admin(property_uid):  # admin view billing list
    statement = """SELECT * FROM Billing b JOIN BaseProperty bp ON bp.PropertyID = b.PropertyID WHERE b.BillingType != 'Rent' AND bp.PropertyUID = ?"""
    return view(statement, property_uid)


def overview_unpaid():  # Overview of unpaid bill
    statement = """SELECT * FROM Billing WHERE PaymentDate IS NULL"""
    unpaid_bill_list = []
    records = Get.read_all(statement=statement)
    for record in records:
        bill = Billing.Billing(record)
        unpaid_bill_list.append(bill.billing_amount)
    return sum(unpaid_bill_list)


def overview(property_id):  # Overview of unpaid bill by property
    statement = """SELECT * FROM Billing WHERE PaymentDate IS NULL AND PropertyID = ?"""
    unpaid_bill_list = []
    records = Get.read_multiple(statement=statement, row_id=property_id)
    for record in records:
        bill = Billing.Billing(record)
        unpaid_bill_list.append(bill.billing_amount)
    return {"property_id": property_id, "total": sum(unpaid_bill_list)}


def view(statement, row_id):
    billing_list = []
    records = Get.read_multiple(statement=statement, row_id=row_id)
    for record in records:
        billing_list.append(vars(Billing.Billing(record)))
    return billing_list
