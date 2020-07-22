import math
from solver.db_connection import db_connect, db_close
import pandas as pd
import matplotlib.pyplot as plt
from solver.utils import merge_all_tables
import numpy as np
import seaborn as sns


"""
Produces scatter graph correlating credit limit and transaction values in fraudulent transactions
Results not insightful
@Params - none
@returns - null
"""

def fraud_credit_limit_transaction_value():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds.plot.scatter(x='credit_limit', y='value')
    a, b = np.polyfit(df_all_frauds.credit_limit, df_all_frauds.value, 1)
    x1 = min(df_all_frauds.credit_limit)
    x2 = max(df_all_frauds.credit_limit)
    plt.plot([x1, x2], [a*x1 + b, a*x2 + b], color='red')
    plt.title("Credit limit and value of fraudulent transaction")
    plt.show()
    db_close(connection, cursor)


"""
Produces pie chart showing distribution of vintage groups in customers that
had fraudulent transactions
@Params - none
@returns - null
"""


def vintage_group_fraud():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds["vintage_group"].value_counts().plot.pie(autopct='%1.1f%%')
    db_close(connection, cursor)
    plt.title("Vintage Groups of Customers With fraudulent transactions")
    plt.show()



"""
Produces pie chart showing distribution of vintage groups in customers 
that did not have fraudulent transactions
@Params - none
@returns - null
"""


def vintage_group_non_fraud():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud["vintage_group"].value_counts().plot.pie(autopct='%1.1f%%')
    db_close(connection, cursor)
    plt.title("Vintage Groups of Customers With No fraudulent transactions")
    plt.show()


"""
Produces histogram showing distribution of fraudulent transaction per month
@Params - none
@returns - null
"""


def fraud_month_distribution():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds["month"] = df_all_frauds["transaction_date"].apply(lambda x: x.month)
    hist = df_all_frauds.month.plot.hist(bins=12, grid=True, color="red", layout = (30, 12))
    plt.xlabel("Month of Transaction")
    plt.ylabel("Frequency of Fraudulent Transactions")
    plt.title("Distribution of Fraudulent Transactions per Month")
    db_close(connection, cursor)
    plt.show()

"""
Produces histogram showing distribution of fraudulent transaction per day in September
@Params - none
@returns - null
"""


def fraud_september_distribution():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_all_frauds["month"] = df_all_frauds["transaction_date"].apply(lambda x: x.month)
    df_all_frauds_september = df_all_frauds[df_all_frauds['month'] == 9]
    df_all_frauds_september["day"] = df_all_frauds_september["transaction_date"].apply(lambda x: x.day)
    hist = df_all_frauds_september.day.plot.hist(bins=15, grid=True, color="orange", layout = (30, 12))
    plt.xlabel("Day of Transaction")
    plt.ylabel("Frequency of Fraudulent Transactions")
    plt.title("Distribution of Fraudulent Transactions per Day in September")
    db_close(connection, cursor)
    plt.show()

"""
Produces categorical graph with values for fraudulent and 
non fraudulent transactions in Segment 11 
@Params - none
@returns - null
"""


def fraud_segment11_distribution():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_fraud_s11 = df_all_frauds[df_all_frauds["transaction_segment"]=="SEG11"]
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud["fraud_flag"] = [False for x in range(len(df_non_fraud))]
    df_non_fraud_s11 = df_non_fraud[df_non_fraud["transaction_segment"]=="SEG11"]
    all_transactions = pd.concat([df_non_fraud_s11, df_fraud_s11], ignore_index=True, sort=False)
    sns.set(style="ticks", color_codes=True)
    sns.catplot(x="transaction_segment", y="value", hue="fraud_flag", data=all_transactions, kind="box")
    plt.title("Segment 11 Values of Fraudulent and Non Fraudulent Transactions")
    plt.show()

"""
Produces histogram showing distribution of fraudulent and non fraudulent
transaction per transaction segment
@Params - none
@returns - null
"""


def fraud_segment_distribution():
    connection, cursor = db_connect()
    df_all_frauds, df_all = merge_all_tables(connection, cursor)
    df_non_fraud = df_all[~df_all["transaction_id"].isin(df_all_frauds["transaction_id"])]
    df_non_fraud["fraud_flag"] = [False for x in range(len(df_non_fraud))]
    all_transactions = pd.concat([df_non_fraud,df_all_frauds], ignore_index=True, sort=False)
    sns.set(style="ticks", color_codes=True)
    sns.catplot(x="transaction_segment", y="value", hue="fraud_flag", data=all_transactions, kind="box")
    plt.title("Segment Values of Fraudulent and Non Fraudulent Transactions")
    plt.show()

