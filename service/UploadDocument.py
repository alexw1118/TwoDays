from data import Connection
import pandas as pd


def upload_properties(value):  # value is .csv file with property list from admin
    statement = """INSERT INTO BaseProperty (PropertyUID, Price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, ExtraRoom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township, Contract, ContactPeriod, RentID, OwnershipID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    token = add_multiple_properties(statement, value)
    return token


def add_multiple_properties(statement, value):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        data = pd.read_csv(value)
        df = pd.DataFrame(data, columns=['PropertyUID', 'Price', 'PropertyType', 'YearBuilt', 'TenureType', 'Bedroom',
                                         'Bathroom', 'ExtraRoom', 'Parking', 'Size', 'FloorPlan', 'Unit', 'Area',
                                         'Street', 'District', 'State', 'Postcode', 'Township', 'Contract',
                                         'ContactPeriod', 'RentID', 'OwnershipID'])
        for row in df.itertuples():
            cursor.execute(statement, row.PropertyUID, row.Price, row.PropertyType, row.YearBuilt, row.TenureType,
                           row.Bedroom, row.Bathroom, row.ExtraRoom, row.Parking, row.Size, row.FloorPlan, row.Unit,
                           row.Area, row.Street, row.District, row.State, row.Postcode, row.Township, row.Contract,
                           row.ContactPeriod, row.RentID, row.OwnershipID)
        connect.commit()
        print("Insertion Successful!")
        return True
    except Exception as error:
        print("Insertion Error: ", error)
        return False
    finally:
        # closing database connection.
        cursor.close()
        connect.close()
        print("Connection Closed!")
