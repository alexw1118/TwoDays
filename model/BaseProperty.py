class BaseProperty:
    def __init__(self, base_property):
        self.property_id = base_property[0]
        self.property_uid = base_property[1]
        self.price = base_property[2]
        self.property_type = base_property[3]
        self.year_built = base_property[4]
        self.tenure_type = base_property[5]
        self.bedroom = base_property[6]
        self.bathroom = base_property[7]
        self.extra_room = base_property[8]
        self.parking = base_property[9]
        self.size = base_property[10]
        self.floor_plan = base_property[11]
        self.unit = base_property[12]
        self.area = base_property[13]
        self.street = base_property[14]
        self.district = base_property[15]
        self.state = base_property[16]
        self.postcode = base_property[17]
        self.township = base_property[18]
        self.contract = base_property[19]
        self.contract_period = base_property[20]
        self.rent_id = base_property[21]
        self.is_deleted = base_property[22]
        self.ownership_id = base_property[23]
        self.furnish = base_property[24]
        self.rent_price = base_property[25]
        self.sell_price = base_property[26]
        self.usage = base_property[27]
        self.free_utility = base_property[28]
        self.images = base_property[29]
        self.rent_start_date = base_property[30]
        self.rent_end_date = base_property[31]
        self.rental_period = base_property[32]
        self.description = base_property[33]
        self.last_updated_date = base_property[34]
        self.rent_contract = base_property[35]
        self.sell_contract = base_property[36]
