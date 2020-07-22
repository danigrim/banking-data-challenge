from solver.utils import db_call_function,merge_all_tables
from solver.data_extraction import print_age_average, cfamily_creditlimit_correlate, highest_value_frauds
from solver.db_connection import db_connect, db_close


def main():
    connection, cursor = db_connect()

    # Average age of customers
    print_age_average(connection, cursor)

    # Card family ranking based on credit limit
    cfamily_creditlimit_correlate(connection, cursor)

    # Ids of frauds with highest values
    highest_value_frauds(connection, cursor)

    db_close(connection, cursor)


main()