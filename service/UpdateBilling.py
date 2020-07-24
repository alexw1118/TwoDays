from data import Put


def modify(value):
    statement = """UPDATE Billing SET IssuedDate = ?, BillingType = ?, BillingAmount = ?, PaymentDate = ?, PropertyID = ? WHERE BillingID = ?"""
    token = Put.update(statement=statement, value=value)
    return token
