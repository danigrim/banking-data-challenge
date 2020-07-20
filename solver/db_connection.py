import psycopg2
from psycopg2 import Error, connect
from solver.credentials import USER, PASSWORD, HOST, PORT,DB_NAME

""" 
Establishes connection to database
 @Params - none
 @Returns - On success: connection, cursor | On failure: null
 """


def db_connect():

    try:
        connection = None

        connection = connect(user = USER,
                            password = PASSWORD,
                            host = HOST,
                            port = PORT,
                            dbname = DB_NAME)

        cursor = connection.cursor()
        print("Successfully connected to database")
        return connection, cursor

    except (Exception, Error) as error:
        print ("Error connecting to database", error)


""" 
Closes connection to database
 @Params - connection, cursor
 @Returns - null
 """


def db_close(connection, cursor):

    if connection:
        cursor.close()
        connection.close()
        print("Connection closed successfully")