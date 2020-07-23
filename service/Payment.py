from data import Put


def pay_bill(payment_date, billing_id):
    statement = """UPDATE Billing SET PaymentDate = %s WHERE BillingID = %s"""
    token = Put.update(statement=statement, value=payment_date, row_id=billing_id)
    return token
