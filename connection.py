import mysql.connector 
def_getconnection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "appdb",
        port = 3306
    )