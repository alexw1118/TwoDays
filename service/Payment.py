from data import Put


def pay(value):
    statement = """UPDATE Billing SET PaymentDate = ? WHERE BillingID = ?"""
    token = Put.update(statement=statement, value=value)
    return token
