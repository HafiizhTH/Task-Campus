import pandas as pd
import numpy as np
import json

df1 = pd.read_csv ('data1.csv')
print (df1)

df2 = pd.read_csv ('data2.csv')
print (df2)

df = pd.concat([df1,df2])
print (df)

df.drop(['color'], axis=1, inplace=True)
print (df)

df.drop(['language'], axis=1, inplace=True)
print (df)

df['director_name'].fillna('N/A', inplace=True)
print(df)

df['gross'].fillna(0, inplace=True)
print(df)

df['movie_title']=df['movie_title'].str.replace('Ã©','e',regex=True)
print(df)

df['country']=df['country'].str.replace('United States','USA',regex=True)
print(df)

df['country']=df['country'].str.upper()
print(df)

df['duration']=np.where(df['duration']<=10,0,df['duration'])
print (df)

df['duration']=np.where(df['duration']>300,0,df['duration'])
print (df)

df['imdb_score']=np.where(df['imdb_score']<=0,0,df['imdb_score'])
print (df)

actors_list = df["actors"].str.split(",",n = 2,expand=True)
df["actor1"]= actors_list[0]
df["actor2"]= actors_list[1]
df["actor3"]= actors_list[2]
print (df)




