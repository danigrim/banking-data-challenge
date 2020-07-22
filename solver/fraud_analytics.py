import math
from solver.db_connection import db_connect, db_close
import pandas as pd
import matplotlib.pyplot as plt
from solver.utils import merge_all_tables


"""
Transaction segments describe for fraudulent and non fraudulent transactions
@Params - none
@Returns - none
"""
def describe_value_segment_transaction(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    print(df_all_frauds.transaction_segment.describe(), "Transaction segment in fraudulent transactions")
    print(df_non_fraud.transaction_segment.describe(), "Transaction segment in non fraudulent transactions")




"""
Values for fraudulent and non fraudulent transactions
@Params - none
@Returns - none
"""

def value_transactions_describe(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds.sort_values(["transaction_date"], inplace=True)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud.sort_values(["transaction_date"], inplace=True)
    print(df_non_fraud.describe(include="all"), "Describe values of non fraudulent transactions")
    print(df_all_frauds.describe(include="all"), "Describe values of fraudulent transactions")



