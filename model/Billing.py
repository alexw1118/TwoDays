class Billing:
    def __init__(self, billing):
        self.billing_id = billing[0]
        self.issue_date = billing[1]
        self.billing_type = billing[2]
        self.billing_amount = billing[3]
        self.payment_date = billing[4]
        self.property_id = billing[5]
