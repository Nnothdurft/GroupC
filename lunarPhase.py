import json
import requests
import csv
import pandas as pd
import numpy as np
import time

datesOnly = []
test = []
lunarPhases = []
preDataDate = pd.datetime(2007,12,31)
crimeData = pd.read_csv("stl-crime-data_2008-2015.csv", low_memory=False)
dates = crimeData["DateOccured"].unique()
for day in dates:
    temp, tm = day.split(" ")
    datesOnly.append(temp)
datesOnly = pd.DataFrame(datesOnly)
datesOnly = datesOnly[0].unique()
datesOnly = pd.DataFrame(datesOnly, columns=["Dates"])
datesOnly["Dates"] = pd.to_datetime(datesOnly["Dates"])
test = datesOnly["Dates"][datesOnly.Dates > preDataDate]
datesOnly = pd.DataFrame(test)
datesOnly = datesOnly.sort_values(by="Dates")
datesOnly["Dates"] = datesOnly["Dates"].apply("{:%m/%d/%Y}".format)
url = "http://api.usno.navy.mil/moon/phase?date="
for date in datesOnly["Dates"]:
    count += 1
    response = requests.get(url + date + "&nump=1&loc=St. Louis").json()
    lunarPhases.append(response["phasedata"][0]["phase"])
    time.sleep(2)
print(lunarPhases)
datesOnly["Phase"] = lunarPhases
datesOnly.to_csv("phaseByDate.csv")