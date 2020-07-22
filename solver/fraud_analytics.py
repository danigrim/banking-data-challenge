import math

import pandas as pd
import matplotlib.pyplot as plt
from solver.utils import db_call_function,merge_all_tables

"""
Pie chart with frauds per segment of customer

"""
def fraud_correlate_customer_segment(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds_unique = df_all_frauds.drop_duplicates(["customer_id"], keep="first")
    df_all_frauds_unique["segment"].value_counts().plot.pie(autopct='%.2f')
    plt.title("Customer segments in fraudulent transactions")
    plt.show()


def non_fraud_customer_segments(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud_unique = df_non_fraud.drop_duplicates(["customer_id"], keep="first")
    df_non_fraud_unique["segment"].value_counts().plot.pie(autopct='%.2f')
    plt.title("Customer segments in non fraudulent transactions")
    plt.show()


def non_fraud_age(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud_unique = df_non_fraud.drop_duplicates(["customer_id"], keep="first")
    print(df_non_fraud_unique.age.describe(), "non fraud age")


def fraud_age(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds_unique = df_all_frauds.drop_duplicates(["customer_id"], keep="first")
    print(df_all_frauds_unique.age.describe(), "fraud age")


# important finding, frauds have almost always only one purchase - first timers?
def customer_frequency_descriptions(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    print(df_all_frauds.describe(include="all"), "fraudulent describe")
    df_non_fraud = df_all[~(df_all["transaction_id"].isin(df_all_frauds["transaction_id"]))]
    print(df_non_fraud.describe(include="all"), "non fraud describe customer frequency")
    print((df_non_fraud["customer_id"].value_counts())) #482 unique customers for 9891 transactions, mean of 20 per person!


def value_first_transaction(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds.sort_values(["transaction_date"], inplace=True)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud.sort_values(["transaction_date"], inplace=True)
    df_non_fraud_first = df_non_fraud.drop_duplicates(["customer_id"], keep="first")
    df_all_frauds_first = df_all_frauds.drop_duplicates(["customer_id"], keep="first")
    print(df_non_fraud_first.describe(include="all"), "non fraud describe first transaction value")
    print(df_all_frauds_first.describe(include="all"), "fraud describe first transaction value")


def vintage_group_fraud(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds["vintage_group"].value_counts().plot.pie(autopct='%.2f')
    plt.title("Vintage groups of fraudulent transactions")
    plt.show()
    #fraud_vg3 = df_all_frauds[df_all_frauds["vintage_group"] == "VG3"]
    #df_non_fraud_vg3 = df_all[(~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])) & df_all["vintage_group"] == "VG1"]
    #print(fraud_vg3.describe(), "Fraudulent VG3")
    #print(df_non_fraud_vg3.describe(), "non fraudulent vg3")

def vintage_group_non_fraud(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud["vintage_group"].value_counts().plot.pie(autopct='%.2f')
    plt.title("Vintage groups of non fraudulent transactions")
    plt.show()

def vintage_group_transaction_correlate_fraud(connection, cursor):
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all["transaction_trimester"] = df_all["transaction_date"].apply(lambda x: (math.ceil((x.month/4))))
    df_all["fraud_flag"] = df_all["transaction_id"].apply(lambda x: .isin(df_all_frauds["transaction_id"]))
    date_correlate = df_all.groupby(["transaction_trimester", "fraud_flag"])
    print(date_correlate.describe())
    # when the vintage group is the same as the month of transaction (recent ?)
    #af_all_frauds



db_call_function(vintage_group_transaction_correlate_fraud)
