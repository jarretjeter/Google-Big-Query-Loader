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


rmn_emprs = DataFrameLoader("./data/roman-emperors.csv")
rmn_emprs.dropna()
rmn_emprs.drop_duplicates()
rmn_emprs.fillna()
rmn_emprs.sort_values("Index")



# project_id = "deb-01-346205"
client = bigquery.Client()

dataset_id = "{}.roman_emperors".format(client.project)

dataset = bigquery.Dataset(dataset_id)

dataset.location = "US"

dataset = client.create_dataset(dataset, timeout=30)

logger.info("Created dataset {}.{}".format(client.project, dataset.dataset_id))