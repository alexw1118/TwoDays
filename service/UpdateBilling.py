from data import Put


def modify(value, billing_id):
    statement = """UPDATE Billing SET IssuedDate = ?, BillingType = ?, BillingAmount = ?, PaymentDate = ?, PropertyID = ? WHERE BillingID = ?"""
    token = Put.update(statement=statement, value=value, row_id=billing_id)
    return token
