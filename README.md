# Logs-Analysis

This Python program queries a PostgresSQL database called "news" in order to return answers the following questions:

* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

The psycopg2 module is used to run queries.

## Requirements
* Python 3.6.2
* Data set entitled `news` available for download [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). 

## Running the Program
* Place unzipped file in directory and use the command `psql -d news -f newsdata.sql` to load data.
* Execute the Python file - `python logs.py`.
