from dagster import asset, get_dagster_logger, Config
from faker import Faker
from datetime import datetime
from lab5.crud.sqlite import *
# Get our Logger
logger = get_dagster_logger()
# Get our data generator
fake = Faker()

##########################################################
################# Insert Code Below ######################
##########################################################

class IngestDataConfig(Config):
    nrows: int = 5

@asset(description="This checks if our table exists")
def create_demo_table():
    logger.info('Create table if it does not exist within our database')
    try:
        create_table()
    except Exception as e:
        logger.error('Had issues with creating the table in the database')
        logger.error(e)

@asset(description="Return metadata for the database before")
def display_table_before(create_demo_table):
    logger.info('Getting the meta data for our database before adding')
    try:
        nrows, ncols = get_table_meta()
        logger.info(f'The table has {nrows} rows\nThe table has {ncols} columns')
    except Exception as e:
        logger.error('Failed to get the table metadata')
        logger.error(e)

@asset(description="This ingests an example bit of data into the database")
def ingest_data(display_table_before, config: IngestDataConfig):
    data = [(int(fake.msisdn()), fake.name(), fake.email(), datetime.now()) for i in range(config.nrows)]
    logger.info(f'Injesting {len(data)} rows into the database')
    try:
        add_data(data)
    except Exception as e:
        logger.error('Failed to ingest data into the database')
        logger.error(e)

@asset(description="Return metadata for the database after")
def display_table_after(ingest_data):
    logger.info('Getting the meta data for our database after adding')
    try:
        nrows, ncols = get_table_meta()
        logger.info(f'The table has {nrows} rows\nThe table has {ncols} columns')
    except Exception as e:
        logger.error('Failed to get the table metadata')
        logger.error(e)

@asset(description="This allows the user to delete all the data from the database")
def clear_table():
    logger.info('Deleting all data from the database.')
    try:
        remove_data('demo')
    except Exception as e:
        logger.error('Failed to clear the database')
        logger.error(e)