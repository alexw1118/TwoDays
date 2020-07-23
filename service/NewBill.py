from data import Post


def create_bill(value):
    statement = """INSERT INTO Billing (IssuedDate, BillingType, BillingAmount, PaymentDate, PropertyID) VALUES (%s, %s, %s, %s, %s)"""
    token = Post.create(statement=statement, value=value)
    return token
