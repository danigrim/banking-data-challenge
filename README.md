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
  Solver - Package folder <br /> 
    |_ consts.py *Names of tables<br />
    |_ data_extraction.py *Functions finding extracting data for part 1<br />
    |_ db_connection.py *Functions establishing and closing connection to PostgreSQL database<br />
    |_ utils.py *Functions implementing functionalities such as merging and sorting tables, getting column names for tables and more<br />
    |_ fraud_analytics.py *Functions performing analysis for part 2<br />

## Answers
----
Part 1 : Data Extraction & Analytics 
----

- What is the average age of the customers in the database

	Answer : The average age of customers in the database is 35 years old <br />
	*File Location: solver/data_extraction.py | Function name: get_age_average


## Clarification points 
- For the analysis pertaining to characteristics of the customer, the command drop_duplicates(["customer_id"], keep="first") was 	used to avoid averages and data distributions to be skewed towards the data for customers that perform multiple transactions. <br />
- This analysis is restricted to the information available in the database. I recognize that, for example, for card family ranking analysis, it is possible that having more data points would lead to different conclusions about the limits of each ranking.

	
