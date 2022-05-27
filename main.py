import mysql.connector 
from mysql.connector import Error
import pandas as pd

def ConnectionFactory(host, name, pwd):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=name,
            passwd=pwd,
            database=name
        )
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

def ExecuteQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database execute query sucessfully")
    except Error as err:
        print(f"Error: '{err}'")


conn = ConnectionFactory("www.mirascraft.ml", "1144331", "mirascraft")
ExecuteQuery(conn, "SELECT `id`, `name`, `size`, `content`, `extension` FROM `File` WHERE 1")