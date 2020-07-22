### Banking Data Challenge
----
This repository contains my answers to the Stone data challenge
----
## Technologies used
  Language: Python
  Python Libraries: 
 		psycopg2 - Used to establish a connection with the PostgreSQL database
    pandas - Used to extract and analyze data from the database
		matplotlib - Used to plot graphs and diagrams 

## Instructions to run
   You must install Python3 with psycopg2, pandas and matplotlib prior to attempting to run
   Run python -m solver.main.py
   Summary of answers and snapshots of data frames will be printed to console in order   
   
## Project Structure
  Solver - Package folder
    |_ consts.py *Names of tables
    |_ data_extraction.py *Functions finding extracting data for part 1
    |_ db_connection.py *Functions establishing and closing connection to PostgreSQL database
    |_ utils.py *Functions implementing functionalities such as merging and sorting tables, getting column names for tables and more
    |_ fraud_analytics.py *Functions performing analysis for part 2 
