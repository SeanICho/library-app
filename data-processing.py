import pandas as pd
import json
from datetime import datetime, time

# def ContainStringRemove (lib, column, string):
#     contains = lib[column].str.contains(string)
#     index = contains[contains == False].index
#     lib.drop(index, inplace=True)
#     print('{} column adjusted!'.format(column))
#
# def RemoveString (lib, column, string):
#     lib[column] = lib[column].str.replace(string, '')
#     print('{} column adjusted!'.format(column))
#
# def TrimColumns (lib, dtype):
#     lib_obj = lib.select_dtypes([dtype])
#     lib[lib_obj.columns] = lib_obj.apply(lambda x: x.str.strip())
#     lib[lib_obj.columns] = lib_obj.apply(lambda x: x.str.strip("))
#     print('all string columns trimmed!')

lib = pd.read_csv("niles_maine_library.csv", index_col=0, encoding="UTF-8")

# ContainStringRemove(lib, 'event_location', 'Niles-Maine District Library')
#
# RemoveString(lib, 'event_group', 'Age group:')
# RemoveString(lib, 'event_type', 'events type:')
# TrimColumns(lib, 'object')

# def TimeSetup (lib, column):
#     lib[column] = lib[column] + ', ' + str(datetime.now().year)
#     index = lib[column].str.index("-")
    # index = lib[column].str.replace("-",)

year = datetime.now().year
# if lib["event_time"].str.endswith(year, na=False).any() == False:
    # lib["event_time"] =  + ', ' + str(year)
# print(lib.event_time)
# notes:  split  with :  -> day, date (current year should be added) -> split with ,
# goal: create start datetime and end datetime

# lib["event_time_day"] = lib["event_time"].str.split(", |: | - ")[0]
lib["event_time_split"] = lib.event_time.str.split(", |: | - ")
# print(lib.event_time_split.head())

lib["event_time_month"] = lib["event_time_split"].apply(lambda x: x[1]).str.split().apply(lambda x: x[0]).map({'January': '1', 'February': '2',  'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'})

lib["event_time_day"] = lib["event_time_split"].apply(lambda x: x[1]).str.split().apply(lambda x: x[1])
print(lib["event_time_day"].head())
# lib["event_time_start_time_am_pm"] = lib["event_time_split"].apply(lambda x: x[2]).str.slice(-2, -1, 1)
# lib["event_time_start_time_hour"] = lib["event_time_split"].apply(lambda x: x[2])#.str.slice(0, -2, 1).str.split().apply(lambda x: int(x[0]) + 12 if lib["event_time_start_time_am_pm"] = 'p')

# lib["event_time_start_time_minute"] = lib["event_time_split"].apply(lambda x: x[2]).str.slice(-4, -2,1)
# pat =
lib["event_time_start_time"] = lib["event_time_split"].apply(lambda x: x[2]).str.replace('am', ' am').str.replace('pm', ' pm').str.split(':| ')

lib["event_time_start_time_hour"] = lib["event_time_start_time"].apply(lambda x: str(int(x[0]) + 12) if x[2] == 'pm' and x[0] != '12' else x[0])
lib["event_time_start_time_minute"] = lib["event_time_start_time"].apply(lambda x: x[1])
lib["event_time_start_time_modified"] = lib["event_time_start_time_hour"] + ":" +  lib["event_time_start_time_minute"]

# print(lib["event_time_start_time_modified"].head())

lib["event_time_end_time"] = lib["event_time_split"].apply(lambda x: x[3]).str.replace('am', ' am').str.replace('pm', ' pm').str.split(':| ')
lib["event_time_end_time_hour"] = lib["event_time_end_time"].apply(lambda x: str(int(x[0]) + 12) if x[2] == 'pm' and x[0] != '12' else x[0])
lib["event_time_end_time_minute"] = lib["event_time_end_time"].apply(lambda x: x[1])
lib["event_time_end_time_modified"] = lib["event_time_end_time_hour"] + ":" +  lib["event_time_end_time_minute"]

# print(lib["event_time_end_time_modified"].head())

lib["event_time_start_time_final"] = lib["event_time_month"] + "/" + lib["event_time_day"] + "/" + str(year) + " " + lib["event_time_start_time_modified"]
lib["event_time_end_time_final"] = lib["event_time_month"] + "/" + lib["event_time_day"] + "/" + str(year) + " " + lib["event_time_end_time_modified"]

lib[["event_time_start_time_final", "event_time_end_time_final"]] = lib[["event_time_start_time_final", "event_time_end_time_final"]].apply(pd.to_datetime)
 # lib["event_time_start_time_final"].apply(lambda x: datetime.datetime.)

# pd.to_datetime(lib["event_time_start_time_final", "event_time_end_time_final"])

print(lib["event_time_start_time_final"].head())
print(lib["event_time_end_time_final"].head())
# print(lib.event_time_day)
# prixnt(type(lib["event_time_day"] ))
# lib["event_time_date"] = lib["event_time"].str.split([", ", ": ", " - "])[1]
# lib["event_time_start_time"] = lib["event_time"].str.split([", ", ": ", " - "])[2]
# lib["event_time_end_time"] = lib["event_time"].str.split([", ", ": ", " - "])[3]
# print(lib["event_time_day"][0])


# index1 = lib.event_time.str.index(":")
# lib["index2"] = lib.event_time.str.index("-")
# print(lib.event_time.str(index1))
# for item in index1.iteritems():
#     print("item: {}".format(item[1]))
# lib["event_from"] = [lib["event_from"].str.slice(0, i) for i in index1.iteritems()]
# print(lib["event_from"])

# print (lib["event_from"])
# print (lib.event_time)


# print(lib.event_time.str.index(":"))
# print(lib.event_time.str.contains("-"))


# lib.to_csv("niles_maine_library.csv")
# print("csv file has been updated!")
#
# # lib = lib.to_json()
# file = open("niles_maine_library.json", "w")
# json.dump(lib, file)
# print("csv file has been updated!")
#
# file.close()
