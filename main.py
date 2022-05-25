from google.cloud import bigquery
import logging
from logging import INFO
import pandas as pd
import pandas_gbq
import sys

logging.basicConfig(format='[%(levelname)-5s][%(asctime)s][%(module)s:%(lineno)04d] : %(message)s',
                    level=INFO,
                    stream=sys.stderr)
logger: logging.Logger = logging

# Reading csv into dataframe and performing transformations, setting inplace=True for each so that no copies are made for this case.
rmn_emprs = pd.read_csv("./data/roman-emperors.csv")
# Column names cannot have white spaces, replacing with underscores
rmn_emprs.rename(columns={"Full Name": "Full_Name", "Birth City": "Birth_City", "Birth Province": "Birth_Province", "Reign Start": "Reign_Start", "Reign End": "Reign_End"}, inplace=True)
# Dropped the unnecessary Unnamed columns that also had NaN values
rmn_emprs.dropna(how="all", axis="columns", inplace=True)
# Drop any potential duplicate rows(there were none)
rmn_emprs.drop_duplicates(inplace=True)
# The Verif column had a lot of NaN values, so I changed them to 0
rmn_emprs.fillna(value=0, inplace=True)
# Returning the dataframe sorted by the Index column orders the emperors first ruler to last. Sorting by Reign_Start isn't quite correct because the date doesn't take into account the years 26 "BC" to 14 "AD" for the ruler Augustus
rmn_emprs.sort_values(by="Index", inplace=True)


# Instantiate my big query client api which will create a dataset
client = bigquery.Client()
# Tell the client to use "bq_code_review" as the dataset name for my project
dataset_id = "{}.bq_code_review".format(client.project)
# Pass dataset_id to bigquery's Dataset class to build a reference
dataset = bigquery.Dataset(dataset_id)
# Assign the datasets server location to us-west2
dataset.location = "us-west2"
# Tell my client to create the dataset on google big query with the completed information
dataset = client.create_dataset(dataset, timeout=30)
# If successful, log the creation of the dataset
logger.info("Created dataset {}.{}".format(client.project, dataset.dataset_id))

# Project to look for when creating a table,
project_id = "deb-01-346205"
# dataset to insert the table into
table_id = "bq_code_review.roman_emperors"

# Loading transformed dataframe into google big query with the specified project/dataset as targets and a specified table schema. load_parquet was the default api_method, and was giving me errors.
pandas_gbq.to_gbq(rmn_emprs, table_id, project_id=project_id, if_exists="replace", api_method="load_csv", table_schema=[
    {'name': 'Index', 'type': 'INT64'}, 
    {'name': 'Name', 'type': 'STRING'}, 
    {'name': 'Full_Name', 'type': 'STRING'}, 
    {'name': 'Birth', 'type': 'STRING'}, 
    {'name': 'Death', 'type': 'STRING'}, 
    {'name': 'Birth_City', 'type': 'STRING'}, 
    {'name': 'Birth_Province', 'type': 'STRING'}, 
    {'name': 'Succession', 'type': 'STRING'}, 
    {'name': 'Reign_Start', 'type': 'STRING'}, 
    {'name': 'Reign_End', 'type': 'STRING'}, 
    {'name': 'Cause', 'type': 'STRING'}, 
    {'name': 'Killer', 'type': 'STRING'}, 
    {'name': 'Dynasty', 'type': 'STRING'}, 
    {'name': 'Era', 'type': 'STRING'}, 
    {'name': 'Notes', 'type': 'STRING'}, 
    {'name': 'Verif', 'type': 'STRING'}, 
    {'name': 'Image', 'type': 'STRING'}])
