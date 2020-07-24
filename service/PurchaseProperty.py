from data import Post, Put


def owned(value):
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township, Contract, ContactPeriod, RentID, OwnershipID, RentPrice, SellPrice, Images, RentalStartDate, RentalEndDate, RentalPeriod, Description, LastUpdatedDate, RentContract, SellContract) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    token = Post.create(statement=statement, value=value)
    return token


def transfer(value, property_uid, ownership_id):
    statement = """UPDATE BaseProperty SET IsDeleted = ? WHERE PropertyUID = ? AND OwnershipID = ?"""
    previous_value = (1, property_uid, ownership_id)
    token = Put.update(statement=statement, value=previous_value)
    if token is True:
        token = owned(value)
    return token
