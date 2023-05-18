from dagster import define_asset_job
from lab5.assets import *

##########################################################
################# Insert Code Below ######################
##########################################################

generate_data_job = define_asset_job(name="generate_data", selection=[create_demo_table, display_table_before, ingest_data, display_table_after])
remove_data_job = define_asset_job(name="remove_data", selection=[clear_table])
