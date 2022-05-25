from google.cloud import bigquery
import logging
from logging import INFO
import os
import pandas as pd
import pandas_gbq
import sys

logging.basicConfig(format='[%(levelname)-5s][%(asctime)s][%(module)s:%(lineno)04d] : %(message)s',
                    level=INFO,
                    stream=sys.stderr)
logger: logging.Logger = logging


class DataFrameLoader():

    def __init__(self, filepath):
        df = pd.read_csv(filepath, header=0)
        self.df = df

    def head(self):
        df = self.df
        return df.head()

    def tail(self):
        df = self.df
        return df.tail()

    def dropna(self):
        df = self.df
        return df.dropna(how="all", axis="columns", inplace=True)

    def drop_duplicates(self):
        df = self.df
        return df.drop_duplicates(inplace=True)

    def fillna(self):
        df = self.df
        return df.fillna(value=0, inplace=True)

    def sort_values(self, col_name):
        df = self.df
        return df.sort_values(by=col_name, inplace=True)

    def dtypes(self):
        df = self.df
        return df.dtypes

    def items(self):
        df = self.df
        for label, content in df.items():
            return f"label: {label}", f"content: {content}"


# rmn_emprs = DataFrameLoader("./data/roman-emperors.csv")
# rmn_emprs.dropna()
# rmn_emprs.drop_duplicates()
# rmn_emprs.fillna()
# rmn_emprs.sort_values("Index")
rmn_emprs = pd.read_csv("./data/roman-emperors.csv")
rmn_emprs.rename(columns={"Full Name": "Full_Name", "Birth City": "Birth_City", "Birth Province": "Birth_Province", "Reign Start": "Reign_Start", "Reign End": "Reign_End"}, inplace=True)
rmn_emprs.dropna(how="all", axis="columns", inplace=True)
rmn_emprs.drop_duplicates(inplace=True)
rmn_emprs.fillna(value=0, inplace=True)
rmn_emprs.sort_values(by="Index", inplace=True)


# credential_path = "/home/jarret/google-creds/deb-01-346205-5113c43e514f.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# class BQLoader():

#     def __init__(self):
#         client = bigquery.Client()
#         self.client = client 
    
#     def create_dataset(self, id:str, location:str) -> None:
#         client = self.client
#         dataset_id = "{}." + f"{id}".format(client.project)
#         dataset = bigquery.Dataset(dataset_id)
#         dataset.location = f"{location}"
#         dataset = client.create_dataset(dataset, timeout=30)
#         logger.info("Created dataset {}.{}".format(client.project, dataset.dataset_id))

# bq_dataset = BQLoader()
# bq_dataset.create_dataset("bq_code_review", "us-west2")


client = bigquery.Client()
dataset_id = "{}.bq_code_review".format(client.project)
dataset = bigquery.Dataset(dataset_id)
dataset.location = "us-west2"
dataset = client.create_dataset(dataset, timeout=30, exists_ok=True)
logger.info("Created dataset {}.{}".format(client.project, dataset.dataset_id))


project_id = "deb-01-346205"
table_id = "bq_code_review.roman_emperors"

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
