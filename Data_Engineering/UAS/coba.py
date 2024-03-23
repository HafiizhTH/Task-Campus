import pandas as pd
import numpy as np
import json
import pyodbc

df1 = pd.read_csv ('data-1.csv')
print (df1)

df2 = pd.read_csv ('data-2.csv')
print (df2)

df = pd.concat([df1,df2])
print (df)

# df.drop(['color'], axis=1, inplace=True)
# print (df)

# df.drop(['language'], axis=1, inplace=True)
# print (df)

df.drop_duplicates(keep='first', inplace=True)
print(df)

df['status'].fillna('N/A', inplace=True)
print(df)

# df['gross'].fillna(0)
# print(df)

hobby_list = df["hobby"].str.split("|",n = 2,expand = True)
df["hobby1"]= hobby_list[0]
df["hobby2"]= hobby_list[1]
df["hobby3"]= hobby_list[2]
print (df)

jsonfilepath = '2012500720.json'

data = {}
with open(csvfilepath) as csvfile:
    csvReader = csv.DictReader(csvfile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows

with open(jsonfilepath, 'w') as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))









