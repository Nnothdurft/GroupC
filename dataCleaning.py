import csv
import pandas as pd

count = 0
df = pd.read_csv("stl-crime-data_2008-2015.csv", header=0, low_memory=False)
df["DateOccured"] = pd.to_datetime(df.DateOccured)
df = df[df.DateOccured >= "2008-01-01"]
df = df[df.UCRType == 1]
df.drop(columns=["PrimeKey", "FileName"], inplace=True)
df.to_csv("crimeData.csv", index=False)