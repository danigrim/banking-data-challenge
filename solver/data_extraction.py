import pandas as pd
import numpy as np
from solver.utils import merge_all_tables, get_unique_customers
import matplotlib.pyplot as plt
import scipy as sp


""" 
Function prints average card holder age
@Returns null
@Params - connection: database connection object, cursor:database cursor object
 """


def print_age_average(connection, cursor):
    cursor.execute("SELECT AVG(age) FROM customers")
    print("The average age of card holders is ")
    print(cursor.fetchone())


""" 
Function analyzes card family ranking based on credit limit. 
Prints description of credit limit distribution within three card families: Gold, Platinum, Premium. 
Prints description of card family distribution within interval that has multiple possibilities for card family
@Returns null
@Params - connection: database connection object, cursor:database cursor object
 """


def cfamily_creditlimit_correlate(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_unique = get_unique_customers(df_all)

    #obtaining entries specific to card families
    df_premium = df_all_unique[df_all_unique['card_family'] == 'Premium']
    df_platinum = df_all_unique[df_all_unique['card_family'] == 'Platinum']
    df_gold = df_all_unique[df_all_unique['card_family'] == 'Gold']

    #printing count, mean, std, min, max and percentile divisions for the credit limit within each card family
    print("Gold Card Family Credit Limits \n", df_gold.credit_limit.describe())
    print("Platinum Card Family Credit Limits \n", df_platinum.credit_limit.describe())
    print("Premium Card Family Credit Limits \n", df_premium.credit_limit.describe())


    # Description of ambiguous interval
    df_intersection = df_all_unique[(df_all_unique['credit_limit'] > 108000) & (df_all_unique['credit_limit'] < 200000)]
    print(df_intersection.card_family.describe(include="all"), "Card Family Rankings in interval of credit limit between R$108000 and R$200000")



""" 
Function prints 95th percentile for value of fraudulent transactions
and data for the 10 highest value fraudulent transactions
@Returns null
@Params - connection: database connection object, cursor:database cursor object
 """


def highest_value_frauds(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds.sort_values(by="value", ascending=False, inplace=True)
    print(df_all_frauds.head(8))
    print("Fraudulent transactions in decreasing order of value \n", df_all_frauds.head())


def plot_fraud_values_hist(connection, cursor):
    #plot histogram with distribution of values above 40000
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds_top = df_all_frauds[(df_all_frauds['value'] > 40000)]
    hist = df_all_frauds_top.value.plot.hist(bins=5)
    plt.xlabel("Value of Transaction ($RS)")
    plt.ylabel("Frequency")
    plt.title("Distribution of values of fraudulent transactions")
    plt.show()


