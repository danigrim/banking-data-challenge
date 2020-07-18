from psycopg2 import sql
from solver.db_connection import db_connect, db_close
from solver.consts import table_names


""" 
Prints column names of table in database
 @Params - Connection: connection to database
 @Returns - null
 """

def get_columns(connection, cursor):
    for table in table_names:
        query_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
        query_str += "table_name = '{}';".format( table )
        column_names = []
        try:
            col_cursor = connection.cursor()
            col_cursor.execute(sql.SQL(query_str).format(sql.Identifier( table )))
            col_names = ( col_cursor.fetchall() )
            for tup in col_names:
                column_names += [ tup[0] ]
        except (Exception) as error:
            print ("Error fetching column names:", error)
        # return the list of column names
        col_cursor.close()
        print(table, column_names)


""" 
Opens database, runs function, closes database
 @Params - func: Function to be executed
 @Returns - null
 """


def db_call_function(func):
    #Connects to database obtaining connection and cursor objects
    connection, cursor = db_connect()
    #calls function
    func(connection, cursor)
    #Closes connection
    db_close(connection, cursor)


db_call_function(get_columns)