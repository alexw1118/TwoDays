class OwnedProperty:
    def __init__(self, owned_property):
        self.ownership_id = owned_property[0]
        self.furnish = owned_property[1]
        self.rent_price = owned_property[2]
        self.sell_price = owned_property[3]
        self.usage = owned_property[4]
        self.status = owned_property[5]
        self.images = owned_property[6]
        self.start_date = owned_property[7]
        self.end_date = owned_property[8]
        self.period = owned_property[9]
        self.description = owned_property[10]
        self.last_updated_date = owned_property[11]
