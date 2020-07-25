from data import Connection
import pandas as pd


def create(statement, value):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        cursor.execute(statement, value)
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


def create_multiple(statement, value):
    try:
        connect = Connection.connection()
        cursor = connect.cursor()
        data = pd.read_csv(value)
        print(data)
        df = pd.DataFrame(data, columns=['PropertyUID', 'Price', 'PropertyType', 'YearBuilt', 'TenureType', 'Bedroom',
                                         'Bathroom', 'ExtraRoom', 'Parking', 'Size', 'FloorPlan', 'Unit', 'Area',
                                         'Street', 'District', 'State', 'Postcode', 'Township', 'Contract',
                                         'ContractPeriod', 'OwnershipID'])
        print(df)
        for row in df.itertuples():
            print(row)
            cursor.execute(statement, row.PropertyUID, row.Price, row.PropertyType, row.YearBuilt, row.TenureType,
                           row.Bedroom, row.Bathroom, row.ExtraRoom, row.Parking, row.Size, row.FloorPlan, row.Unit,
                           row.Area, row.Street, row.District, row.State, row.Postcode, row.Township, row.Contract,
                           row.ContractPeriod, row.OwnershipID)
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