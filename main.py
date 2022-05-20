import pandas as pd

class DataFrameLoader():

    def __init__(self, filepath):
        df = pd.read_csv(filepath, header=0)
        self.df = df
        return df


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