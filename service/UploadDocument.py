from data import Post


def send(csv_file):  # value is .csv file with property list from admin
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township, Contract, ContractPeriod, OwnershipID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    token = Post.create_multiple(statement=statement, value=csv_file)
    return token


def register_Property(value):
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    token = Post.create(statement=statement, value=value)
    return token
