from data import Post, Put


def owned(value):
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township, Contract, ContactPeriod, RentID, OwnershipID, RentPrice, SellPrice, Images, RentalStartDate, RentalEndDate, RentalPeriod, Description, LastUpdatedDate, RentContract, SellContract) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    token = Post.create(statement=statement, value=value)
    return token


def transfer(value, is_deleted, property_id, ownership_id):
    statement = """UPDATE BaseProperty SET IsDeleted = ? WHERE PropertyUID = ? AND OwnershipID = ?"""
    token = Put.update(statement=statement, value=is_deleted, row_id_1=property_id, row_id_2=ownership_id)
    if token is True:
        token = owned(value)
    return token
