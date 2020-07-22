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

## What is the average age of the customers in the database <br />

**Answer** :  < br/>The average age of customers in the database is 35 years old <br />

**File Location**: solver/data_extraction.py | **Function name**: get_age_average

## How is the card_family ranked based on the credit_limit given to each card? <br />

**Answer** : < br/> The three tiers of card family are Gold, Platinum and Premium in increasing order of credit limit. The cards with the lowest limits, between **R$ 2000-50000**, are ranked as **Gold**. The cards with the highest credit limits, between **R$200000-899000**,  are ranked as **Premium**. The cards with a credit limit between **R$51000-108000** are ranked as **Platinum**, although these constitute **only 31% of the Platinum cards.** The cards with a credit limit between **R$108000-200000** can either be ranked as **Premium or Platinum**. It is relevant to note that **78%** of the cards within this interval are ranked as **Platinum**, and 69% of the Platinum cards are in this interval. Moreover, within this credit limit, there is no indication that the choice of ranking between Platinum and Premium depends on their proximity to the higher or lower ends of the interval.**Based on that, it is safe to assume that there exists other variables that influence the ranking of a card as Premium within this interval**. I investigated the possibility of the ranking in this category being related to the customer segment (Gold or Diamond) or the customer Vintage Group (VG1, VG2, VG3) but neither of those factors seem related to the ranking of the card family. It seems most likely that there are extraneous variables influencing the classification within this interval. This could be the case if, for example, customers with a credit limit above R$108000 were given the option to pay the additional fee to get Premium benefits.

**Summarizing Table


**File Location**: solver/data_extraction.py | **Function name**: cfamily_creditlimit_correlate

## For the transactions flagged as fraud, what are the ids of the transactions with the highest value? <br />

**Note** For this question, I considered the “highest value” transactions to be those above the 95th percentile of the distribution of the fraudulent transaction values. The 95th percentile is R$ 48381.8, found using the command ```df_all_frauds.value.quantile([0.95])```

**Answer** <br /> 
Table showing ids of fraudulent transactions with the top 5% of transaction value. The first row is the id of the transaction of highest value, which has value of R$49155.00 


**File Location**: solver/data_extraction.py | **Function name**:  highest_value_frauds



## Clarification points 
- For the analysis pertaining to characteristics of the customer, the command ```drop_duplicates(["customer_id"], keep="first")``` was 	used to avoid averages and data distributions to be skewed towards the data for customers that perform multiple transactions. <br />
- This analysis is restricted to the information available in the database. I recognize that, for example, for card family ranking analysis, it is possible that having more data points would lead to different conclusions about the limits of each ranking.

	
