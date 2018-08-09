import pandas as pd

crimeData = pd.read_csv("crimeData.csv", low_memory=False)
phases = pd.read_csv("phaseByDate.csv")
crimeData.DateOccured = pd.to_datetime(crimeData.DateOccured).dt.date
phases.Dates = pd.to_datetime(phases.Dates).dt.date
phases.drop(columns=["Unnamed: 0"], inplace=True)
crimeData = crimeData.merge(phases, how="inner", left_on="DateOccured", right_on="Dates")
crimeData.drop(columns=["Dates"], inplace=True)
crimeData.to_csv("crimeDataWithPhase.csv", index=False)