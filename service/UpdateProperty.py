from data import Put


def modify(value):
    statement = """UPDATE BaseProperty SET Furnish = ?, RentPrice = ?, SellPrice = ?, Usage = ?, FreeUtility = ?, Images = ?, RentalStartDate = ?, RentalEndDate = ?, RentalPeriod = ?, Description = ?, LastUpdatedDate = ?, RentContract = ?, SellContract = ? WHERE PropertyID = ?"""
    token = Put.update(statement=statement, value=value)
    return token
