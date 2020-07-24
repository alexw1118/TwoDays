from data import Put


def modify(value, property_id):
    statement = """UPDATE BaseProperty SET Furnish = ?, RentPrice = ?, SellPrice = ?, Usage = ?, FreeUtility = ?, Images = ?, RentalStartDate = ?, RentalEndDate = ?, RentalPeriod = ?, Description = ?, LastUpdatedDate = ?, RentContract = ?, SellContract = ? WHERE PropertyID = ?"""
    token = Put.update(statement=statement, value=value, row_id=property_id)
    return token
