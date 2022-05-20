import pandas as pd


def csv_reader(csv_file) -> None:
    return pd.read_csv(csv_file, header=0)



rmn_emprs = csv_reader("./data/roman-emperors.csv")
rmn_emprs = rmn_emprs.dropna(how="all", axis="columns")