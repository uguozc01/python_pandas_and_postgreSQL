## Use Python Pandas library to process postgresql queries or csv files.

    The purpose of this small coding practice is to give an idea 
    how to use python coding effectively in postgreSQL database queries.


## Technologies: pandas, postgresql and sqlalchemy. Why Pandas?

    Pandas library was developed on the top of Numpy library. 
    So, many functions rely on C coding behind the scenes and this makes it fast. 
    
    But how? Imagine you have a python list and if you want to process this list in an ordinary way, 
    python allocates a random memory for each element of the list however in numpy and pandas 
    memory allocation for arrays are mostly done as a block in memory, a better organised way. 
    This also provides releasing memory faster when an operation process ends. Besides, 
    sorting algorithms are based on optimised C coding/sorting algorithms.

    You can also have a look at this video link and see how fast iterations are in numpy (so
    how fast things are in pandas).
    https://www.youtube.com/watch?v=Qgevy75co8c


## Installation

    pip install pandas
    pip install psycopg2
    pip install sqlalchemy


### Where to start, how to approach sql processing in python?

    1. Create a credentials file.

        This could be a .yaml or .pgpass file. In my case I used yaml file.
        On Unix systems, the permissions on .pgpass or .yaml must disallow any access to world or group; 
        achieve this by the command 
**chmod 0600 ~/.pgpass  or  chmod 0600 ~/.yaml**

    2. Create a generic database connection script so that you can always call it in other scripts.

        Please check setup_environment.py code. In this code simply the following three functions are used.

        ```python
        def get_database():
            ''' call get_connection function in try-except blcok'''
        def get_connection_from_profile(config_file_name):
            ''' Sets up database connection from config file'''
        def get_engine(db, user, host, port, passwd):
            return engine
        ```

        It returns an engine object to crease the connection in next step like:
        engine = setup_environment.get_database()

    3. Create script files for each operations like CSV processing, inserting to db from excel, different
    select queries. In my case I created db table from CSV file:

        Create a script file to process CSV files chunk by chunk:
        
        Create connection from sqlalchemy engine object.
        create a data frame to read from CSV file like the following by providing chunk size:

**df_tips = pd.read_csv**

        Iterate through every chunk in foor loop until all CSV file is completely processed 
        by using pandas "to_sql" method.

        There are more methods like to_excel, to_csv and more.

    4. After database created you can crete another script and trigger an sql query inside the script:
        Check "pandas_fetch.py" script file.

    Similarly you can create many generic scripts to run with parameters for different operations.
    You can fetch some data from database by using a complex SELECT query and you can put it
    into an excel sheet. You can create many scripts. Pandas does not restrict you with only
    relational databases, you can use pandas from reading a mongo database and you can use
    to_json, to_dict methods. It's all upto you. Have a look at all the to_XXX methods:

    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html


### Summary:

        Pandas dataframes in python scripts could be used together with serialisation & deserialisation
    process such as pickling and unpickling. What serialisation offers is that you can store your chunks
    (dataframes) as serialised to transmit or reconstruct for later processing.




