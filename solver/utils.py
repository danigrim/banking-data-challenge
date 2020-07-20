from psycopg2 import sql
from solver.db_connection import db_connect, db_close
from solver.consts import table_names
import pandas as pd

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

""" 
Merges tables transaction
 @Params - 
 @Returns - merged tables
 """
def merge_all_tables(connection, cursor):
    df_frauds = pd.read_sql_query('select * from frauds', con=connection)
    df_transactions = pd.read_sql_query('select * from transactions', con=connection)
    df_transactions.rename(columns={'segment': 'transaction_segment', 'id': 'transaction_id'}, inplace=True)
    df_fraud_transactions = pd.merge(left=df_transactions, right=df_frauds, left_on="transaction_id", right_on="transaction_id", copy=False)
    df_fraud_transactions.sort_values(by="value", ascending=False, inplace=True)
    df_customers = pd.read_sql_query('select * from customers', con=connection)
    df_cards = pd.read_sql_query('select * from cards', con=connection)
    df_customer_cards = pd.merge(left=df_customers, right=df_cards, left_on="id", right_on="customer_id",copy=False)
    df_customer_cards.drop("id", axis=1, inplace=True)

    df_all_frauds = pd.merge(left=df_customer_cards, right=df_fraud_transactions, left_on="card_number", right_on="card_number", copy=False)

    df_all = pd.merge(left=df_customer_cards, right=df_transactions, left_on="card_number", right_on="card_number", copy=False)

    print(df_all_frauds.head(100), "frauds")
    print(df_all.head(100), "not frauds")
    return df_all_frauds, df_all

