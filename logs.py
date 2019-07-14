import psycopg2

views = '''
CREATE VIEW author_views AS 
  select title, name 
  from articles join authors 
  on articles.author = authors.id;
CREATE VIEW article_views AS 
  select title, count(*) as views 
  from articles join log 
  on SUBSTRING(path, 10) = articles.slug group by title;
CREATE VIEW error_rate AS 
  select date, ErrorCount, total, (errorcount * 1.0)/(total * 1.0) as errorrate 
    from (select DATE(time), count(*) total, sum(case when status != '200 OK' then 1 else 0 end) ErrorCount 
      from log group 
      by DATE(time)) error_dates;

'''

top_3_query = '''
  SELECT * from article_views 
  LIMIT 3
  '''

top_author_query = '''
  SELECT name, sum(article_views.views) as views 
  FROM author_views join article_views 
  ON article_views.title = author_views.title 
  GROUP by name 
  ORDER by views DESC;
  '''

error_day_query = '''
  SELECT date, errorrate
  FROM error_rate 
  WHERE errorrate >.01;
  '''

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

def createViews(filename):
    c.execute(filename)

def get_top_3():
  # Create the first two views needed for this query
  #c.execute(sqlCommands[0])
  #c.execute(sqlCommands[1])
  c.execute(top_3_query)
  posts = c.fetchall()
  print "The top 3 articles by view are:"
  for i in posts:
        print(str(i[0]) + ' - ' + str(i[1]) + ' views')
  print "\t"
  db.close

def get_top_author():
  c.execute(top_author_query)
  posts = c.fetchall()
  print "Authors organized by view:"
  for i in posts:
        print(str(i[0]) + ' - ' + str(i[1]) + ' views')
  print "\t"
  db.close

def get_error_day():
  c.execute(error_day_query)
  posts = c.fetchall()
  print "Days in which error rate was over .01%:"
  for i in posts:
        print(str(i[0]) + ' - ' + str(round(i[1],3)) + ' error rate')
  print "\t"
  db.close

if __name__ == '__main__':
  createViews(views)
  get_top_3()
  get_top_author()
  get_error_day()
