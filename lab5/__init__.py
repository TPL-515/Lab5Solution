from dagster import Definitions, load_assets_from_modules

##########################################################
################# Insert Code Below ######################
##########################################################

from lab5 import assets
from lab5.jobs import generate_data_job, remove_data_job

assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=assets,
    jobs=[generate_data_job, remove_data_job]
)