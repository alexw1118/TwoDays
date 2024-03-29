import pyodbc
import config


def connection():
    try:
        conn = pyodbc.connect(
            "Driver={" + config.DATABASE_DRIVER + "};"
            "Server=" + config.DATABASE_SERVER + ";"
            "Database=" + config.DATABASE_NAME + ";"
            "Trusted_Connection=" + config.DATABASE_TRUSTED_CONNECTION + ";"
        )
        return conn
    except Exception as error:
        print("Connection Error: ", error)
        return None
