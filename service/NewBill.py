from data import Post


def create(value):
    statement = """INSERT INTO Billing (IssuedDate, BillingType, BillingAmount, PaymentDate, PropertyID) VALUES (?, ?, ?, ?, ?)"""
    token = Post.create(statement=statement, value=value)
    return token
