import pandas as pd
import json
from datetime import datetime, time

def ContainStringRemove (df, column, string):
    contains = df[column].str.contains(string)
    index = contains[contains == False].index
    df.drop(index, inplace=True)
    print('{} column adjusted!'.format(column))

def RemoveString (df, column, string):
    df[column] = df[column].str.replace(string, '')
    print('{} column adjusted!'.format(column))

def TrimObjectColumns (df):
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    # df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip("))
    print('all string columns trimmed!')

def DateTimeSetup (df, column):
    year = datetime.now().year
    df["split"] = df[column].str.split(", |: | - ")
    df["month"] = df["split"].apply(lambda x: x[1]).str.split().apply(lambda x: x[0]).map({'January': '1', 'February': '2',  'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'})
    df["day"] = df["split"].apply(lambda x: x[1]).str.split().apply(lambda x: x[1])
    df["start_time"] = df["split"].apply(lambda x: x[2]).str.replace('am', ' am').str.replace('pm', ' pm').str.split(':| ')
    df["start_time_hour"] = df["start_time"].apply(lambda x: str(int(x[0]) + 12) if x[2] == 'pm' and x[0] != '12' else x[0])
    df["start_time_minute"] = df["start_time"].apply(lambda x: x[1])
    df["start_time_modified"] = df["start_time_hour"] + ":" +  df["start_time_minute"]
    df["end_time"] = df["split"].apply(lambda x: x[3]).str.replace('am', ' am').str.replace('pm', ' pm').str.split(':| ')
    df["end_time_hour"] = df["end_time"].apply(lambda x: str(int(x[0]) + 12) if x[2] == 'pm' and x[0] != '12' else x[0])
    df["end_time_minute"] = df["end_time"].apply(lambda x: x[1])
    df["end_time_modified"] = df["end_time_hour"] + ":" +  df["end_time_minute"]

    df["event_start_time"] = df["month"] + "/" + df["day"] + "/" + str(year) + " " + df["start_time_modified"]
    df["event_end_time"] = df["month"] + "/" + df["day"] + "/" + str(year) + " " + df["end_time_modified"]

    df[["event_start_time", "event_end_time"]] = df[["event_start_time", "event_end_time"]].apply(pd.to_datetime)

    print("Column " + column + " has been updated!")

    df.drop(["split", "month", "day", "start_time", "start_time_hour", "start_time_minute", "start_time_modified", "end_time", "end_time_hour", "end_time_minute", "end_time_modified"], axis = 1, inplace = True)


niles = pd.read_csv("niles_maine_library.csv", index_col=0, encoding="UTF-8")

ContainStringRemove(niles, 'event_location', 'Niles-Maine District Library')
RemoveString(niles, 'event_group', 'Age group:')
RemoveString(niles, 'event_type', 'events type:')
TrimObjectColumns(niles)
DateTimeSetup (niles, "event_time")

niles.to_csv("niles_maine_library.csv")
print("csv file has been updated!")
#
lib = niles.to_json()
file = open("niles_maine_library.json", "w")
json.dump(lib, file)
print("csv file has been updated!")

file.close()
