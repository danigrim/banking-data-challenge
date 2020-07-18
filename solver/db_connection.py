import psycopg2
from psycopg2 import Error, connect
from solver.credentials import USER, PASSWORD, HOST, PORT,DB_NAME
from solver.utils import get_columns

## Establishing connection to database
try:
    connection = None
    connection = connect(user = USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT,
                                dbname = DB_NAME)
    cursor = connection.cursor()
    print("Successfully connected to database")

except (Exception, Error) as error:
    print ("Error connecting to database", error)

#Prints dictionary with keys of table names and values of table columns then closes connection
finally:
    table_columns = {}
    if(connection):
        table_columns["customers"] = get_columns("customers", connection)
        table_columns["cards"] = get_columns("cards", connection)
        table_columns["transactions"] = get_columns("transactions", connection)
        table_columns["frauds"] = get_columns("frauds", connection)
        print(table_columns)
        cursor.close()
        connection.close()
        print("Connection closed successfully")