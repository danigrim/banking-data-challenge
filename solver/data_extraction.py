import pandas as pd
from solver.utils import db_call_function

""" 
Function prints average customer age
@Returns null
@Params - connection: database connection object, cursor:database cursor object
 """


def get_age_average(connection, cursor):
    query_str = "SELECT AVG(age) FROM customers"
    cursor.execute(query_str)
    avg = cursor.fetchall()
    print(avg)


db_call_function(get_age_average)