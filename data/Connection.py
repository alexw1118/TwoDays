import pyodbc


class Connection:
    def __init__(self):
        self.connection();

    @staticmethod
    def connection():
        conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-98SH10H;"  # Server name
            "Database=TwoDays;"        # Database name
            "Trusted_Connection=yes;"
        )
        return conn.open()
