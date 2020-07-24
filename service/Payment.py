from data import Put


def pay(payment_date, billing_id):
    statement = """UPDATE Billing SET PaymentDate = ? WHERE BillingID = ?"""
    token = Put.update(statement=statement, value=payment_date, row_id=billing_id)
    return token
