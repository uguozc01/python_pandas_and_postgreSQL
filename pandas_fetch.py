import pandas as pd
import psycopg2 as pg
from setup import setup_environment

sql_query = ''' SELECT weekday, 
    ROUND( CAST(SUM (meal_total) as numeric),2) as meal_total, 
    ROUND( CAST(SUM (tip) as numeric),2) as tip_total 
    FROM tips 
    GROUP BY weekday 
    ORDER BY SUM (tip) DESC;'''

def pandas_fetch(sql_query):
    try:
        # create connection to db
        engine = setup_environment.get_database()
        cxn = engine.connect()

    except (Exception, pg.Error) as error:
        print(f'Error occured while connecting to PostgreSQL, {error}')
    
    else:
        df_aggregate = pd.read_sql_query(sql_query, con=cxn)
        print(df_aggregate)

    finally:
        # close database connection
        if cxn:
            cxn.close()
            print('DB connection is now closed')
            
pandas_fetch(sql_query)