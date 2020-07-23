from data import Post


def send(csv_file):  # value is .csv file with property list from admin
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township, Contract, ContactPeriod, RentID, OwnershipID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    token = Post.create_multiple(statement=statement, value=csv_file)
    return token
