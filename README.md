# Logs-Analysis
This program was created as part of the Full Stack NanoDegree program with Udacity, and explores basic concepts regarding python, relational databases, queries and views. For this project, my task was to create a reporting tool that prints out reports in plain text. The program uses the `psycopg2` module to query a mock PostgresSQL database that represents a ficitional news website and returns answers to following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Requirements
* Python 2.7.12
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Data set entitled `news` available for download [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). 

## Running the Program

* Download and install Vagrant. Instructions are found [here](https://www.vagrantup.com/).

* Download and install VirtualBox. Instructions are found [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

* Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder. 

* Run `vagrant up` to bring the virtual machine online. 

* Run `vagrant ssh` to login.

* Navigate to the vagrant directory.

* Load the database using `psql -d news -f newsdata.sql`. 

* Connect to the database using `psql -d news`.

* Create the the following views used to answer questions 2 and 3: 

```sql
CREATE VIEW author_views AS
  select title, name
  from articles join authors
  on articles.author = authors.id;
```

```sql
CREATE VIEW article_views AS
  select title, count(*) as views 
  from articles join log
  on SUBSTRING(path, 10) = articles.slug group by title;
```

```sql
CREATE VIEW error_rate AS
  select date, ErrorCount, total, (errorcount * 1.0)/(total * 1.0) as errorrate 
    from (select DATE(time), count(*) total, 
      sum(case when status != '200 OK' then 1 else 0 end) ErrorCount 
      from log group 
      by DATE(time)) error_dates;
```

* Exit `psql` 

* Execute the Python file - `python logs.py`.
