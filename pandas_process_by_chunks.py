import pandas as pd
import psycopg2 as pg
from setup import setup_environment
import time

def process_csv_by_chunks(chnk):
    try:
        # create connection to db
        engine = setup_environment.get_database()
        cxn = engine.connect()

    except (Exception, pg.Error) as error:
        print(f'Error occured while connecting to PostgreSQL, {error}')
    
    else:
        df_tips = pd.read_csv('/home/uguozc01/myPython/PostgreSQL/tips.csv', header=0, chunksize=chnk)
        for idx, chunk in enumerate(df_tips, start=1): # used enum in case different process depending on rows is needed
            tic = time.perf_counter()
            chunk.to_sql('tips', cxn, index=False, if_exists='append')
            toc = time.perf_counter()
            print(f'chunk{idx} has been processed in {round(toc - tic, 4)} seconds')  # You can remove time measuring lines
        return df_tips

    finally:
        # close database connection
        if cxn:
            cxn.close()
            print('DB connection is now closed')

test_df = process_csv_by_chunks(50)