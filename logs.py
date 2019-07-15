#!/usr/bin/python

import psycopg2

top_3_query = \
    '''
  SELECT * from article_views
  ORDER by views DESC
  LIMIT 3;
  '''

top_author_query = \
    '''
  SELECT name, sum(article_views.views) as views
  FROM author_views join article_views
  ON article_views.title = author_views.title
  GROUP by name
  ORDER by views DESC;
  '''

error_day_query = \
    '''
  SELECT date, errorrate
  FROM error_rate
  WHERE errorrate >.01;
  '''

DBNAME = 'news'
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


def get_top_3():
    c.execute(top_3_query)
    posts = c.fetchall()
    print 'The top 3 articles by view are:'
    for i in posts:
        print str(i[0]) + ' - ' + str(i[1]) + ' views'
    print '\t'
    db.close


def get_top_author():
    c.execute(top_author_query)
    posts = c.fetchall()
    print 'Authors organized by view:'
    for i in posts:
        print str(i[0]) + ' - ' + str(i[1]) + ' views'
    print '\t'
    db.close


def get_error_day():
    c.execute(error_day_query)
    posts = c.fetchall()
    print 'Days in which error rate was over .01%:'
    for i in posts:
        print str(i[0]) + ' - ' + str(round(i[1], 3) * 100) \
            + '% error rate'
    print '\t'
    db.close


if __name__ == '__main__':
    createViews(views)
    get_top_3()
    get_top_author()
    get_error_day()
