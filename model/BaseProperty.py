class BaseProperty:
    def __init__(self, base_property):
        self.property_id = base_property[0]
        self.price = base_property[1]
        self.property_type = base_property[2]
        self.year_built = base_property[3]
        self.tenure_type = base_property[4]
        self.bedroom = base_property[5]
        self.bathroom = base_property[6]
        self.parking = base_property[7]
        self.size = base_property[8]
        self.floor_plan = base_property[9]
        self.unit = base_property[10]
        self.area = base_property[11]
        self.street = base_property[12]
        self.district = base_property[13]
        self.state = base_property[14]
        self.postcode = base_property[15]
        self.township = base_property[16]
        self.ownership_id = base_property[17]
        self.rent_id = base_property[18]
        self.contract_period = base_property[19]
