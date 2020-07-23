from data import Put


def modify(value, property_id):
    statement = """UPDATE BaseProperty SET Furnish = %s, RentPrice = %s, SellPrice = %s, Usage = %s, FreeUtility = %s, Images = %s, RentalStartDate = %s, RentalEndDate = %s, RentalPeriod = %s, Description = %s, LastUpdatedDate = %s, RentContract = %s, SellContract = %s WHERE PropertyID = %s"""
    token = Put.update(statement=statement, value=value, row_id=property_id)
    return token
