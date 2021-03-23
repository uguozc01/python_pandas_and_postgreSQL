import yaml, logging, os
from sqlalchemy import create_engine

os.chdir(os.path.dirname(os.path.abspath(__file__)))
log = logging.getLogger(__name__)


def get_database():
    try:
        engine = get_connection_from_profile()
    except IOError:
        log.exception("Failed to get database connection!")
        return None, 'fail'
    else:
        log.info("Connected to PostgreSQL database!")

    return engine


def get_connection_from_profile(config_file_name="database_cred.yaml"):
    """
    Sets up database connection from config file.
    """
    with open(config_file_name, 'r') as rf:
        vals = yaml.safe_load(rf)

    if not ('PGHOST' in vals.keys() and 'PGPORT' in vals.keys() and 'PGDATABASE' in vals.keys() and 'PGUSER' in vals.keys() and 'PGPASSWORD' in vals.keys()):
        raise Exception('Bad config file: ' + config_file_name)

    return get_engine(vals['PGDATABASE'], vals['PGUSER'], vals['PGHOST'], vals['PGPORT'], vals['PGPASSWORD'])

def get_engine(db, user, host, port, passwd):

    url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'
    engine = create_engine(url, pool_size=50)
    return engine