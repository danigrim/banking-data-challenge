from psycopg2 import sql

# Gets column names from specified table
def get_columns(table, connection):
    col_cursor = connection.cursor()
    query_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
    query_str += "table_name = '{}';".format( table )
    column_names = []
    try:
        col_cursor.execute(sql.SQL(query_str).format(sql.Identifier( table )))
        col_names = ( col_cursor.fetchall() )
        for tup in col_names:
            column_names += [ tup[0] ]
        col_cursor.close()

    except (Exception) as error:
        print ("Error fetching column names:", error)
    # return the list of column names
    return column_names
