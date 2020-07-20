import pandas as pd
from solver.utils import db_call_function,merge_all_tables

""" 
Function prints average customer age
@Returns null
@Params - connection: database connection object, cursor:database cursor object
 """


def get_age_average(connection, cursor):
    cursor.execute("SELECT AVG(age) FROM customers")
    print(cursor.fetchall())

""" 
Function analyzes ranking based on 
@Returns null
@Params - connection: database connection object, cursor:database cursor object
 """


def cardfamily_ranking(connection, cursor):
    cursor.execute("SELECT MIN(credit_limit) FROM cards WHERE card_family='Gold'")
    print(cursor.fetchall(), "GOLD MIN")
    cursor.execute("SELECT MAX(credit_limit) FROM cards WHERE card_family='Gold'")
    print(cursor.fetchall(),"GOLD MAX")
    cursor.execute("SELECT AVG(credit_limit) FROM cards WHERE card_family='Gold'")
    print(cursor.fetchall(), "GOLD AVG")
    cursor.execute("SELECT MIN(credit_limit) FROM cards WHERE card_family='Platinum'")
    print(cursor.fetchall(), "PLAT MIN")
    cursor.execute("SELECT MAX(credit_limit) FROM cards WHERE card_family='Platinum'")
    print(cursor.fetchall(), "PLAT MAX")
    cursor.execute("SELECT AVG(credit_limit) FROM cards WHERE card_family='Platinum'")
    print(cursor.fetchall(), "PLAT AVG")
    cursor.execute("SELECT MIN(credit_limit) FROM cards WHERE card_family='Premium'")
    print(cursor.fetchall(), "PRE MIN")
    cursor.execute("SELECT MAX(credit_limit) FROM cards WHERE card_family='Premium'")
    print(cursor.fetchall(), "PRE MAX")
    cursor.execute("SELECT AVG(credit_limit) FROM cards WHERE card_family='Premium'")
    print(cursor.fetchall(), "PRE AVG")


def cardfamily_ranking(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_plat = df_all[(df_all['card_family'] == 'Premium') & (df_all['credit_limit'] < 200000) & (df_all['segment']!= 'Gold')]
    print(df_all_plat.head(15))


def highest_value_frauds(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds.sort_values(by="value", ascending=False, inplace=True)
    print(df_all_frauds.head())
    return df_all_frauds


def fraud_correlate(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    frauds_vg1 = df_all[(df_all['card_family'] == 'Premium') & (df_all['credit_limit'] < 200000) & (df_all['segment_x']!= 'Gold')]
    cursor.execute("SELECT segment FROM customers WHERE id IN (SELECT customer_id FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id IN (SELECT transaction_id FROM frauds)))")
    cursor.execute("SELECT vintage_group FROM customers WHERE id IN (SELECT customer_id FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id IN (SELECT transaction_id FROM frauds)))")
    #print(cursor.fetchall(), "Max age fraud")
    cursor.execute("SELECT vintage_group FROM customers WHERE id IN (SELECT customer_id FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id NOT IN (SELECT transaction_id FROM frauds)))")
    #print(cursor.fetchall(), "Max age non fraud")
    cursor.execute("SELECT AVG(credit_limit) FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id IN (SELECT transaction_id FROM frauds))")
    #print(cursor.fetchall(), "C limit fraud")
    cursor.execute("SELECT AVG(credit_limit) FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id NOT IN (SELECT transaction_id FROM frauds))")
    #print(cursor.fetchall(), "C limit not fraud")
    cursor.execute("SELECT MAX(credit_limit) FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id IN (SELECT transaction_id FROM frauds))")
    print(cursor.fetchall(), "C limit fraud max")
    cursor.execute("SELECT MAX(credit_limit) FROM cards WHERE card_number IN (SELECT card_number FROM transactions WHERE id NOT IN (SELECT transaction_id FROM frauds))")
    print(cursor.fetchall(), "C limit not fraud MAX")

#def dates_transaction(connection, cursor):
   # cursor.execute("SELECT transaction_date FROM transactions")
   # print(cursor.fetchall())

def all_table(connection, cursor):
    merge_all_tables(connection, cursor)
    pass

db_call_function(cardfamily_ranking)