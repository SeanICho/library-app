import pandas as pd

def ContainStringRemove (df, column, string):
    contains = df[column].str.contains(string)
    index = contains[contains == False].index
    df.drop(index, inplace=True)
    print('{} column adjusted!'.format(column))

def RemoveString (df, column, string):
    df[column] = df[column].str.replace(string, '')
    print('{} column adjusted!'.format(column))

def TrimColumns (df, dtype):
    df_obj = df.select_dtypes([dtype])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    print('all string columns trimmed!')

df = pd.read_csv("niles_maine_library.csv", index_col=0, encoding="UTF-8")

ContainStringRemove(df, 'event_location', 'Niles-Maine District Library')

RemoveString(df, 'event_group', 'Age group:')
RemoveString(df, 'event_type', 'events type:')
TrimColumns(df, 'object')

df.to_csv("niles_maine_library.csv")
print("csv file has been updated!")
