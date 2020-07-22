from solver.utils import merge_all_tables
from solver.data_extraction import print_age_average, cfamily_creditlimit_correlate, highest_value_frauds
from solver.db_connection import db_connect, db_close
from solver.fraud_analytics import value_transactions_describe, describe_value_segment_transaction


def main():
    connection, cursor = db_connect()

    # Average age of customers
    print_age_average(connection, cursor)
    # Card family ranking based on credit limit
    cfamily_creditlimit_correlate(connection, cursor)
    # Ids of frauds with highest values
    highest_value_frauds(connection, cursor)

    #Prints discription of values of transactions, fraudulent and not
    value_transactions_describe(connection, cursor)
    #Prints segment of transactions, fraudulent and not
    describe_value_segment_transaction(connection, cursor)

    db_close(connection, cursor)



main()