import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("officesuppliesnew.csv")
region = df['Region'].unique()
unit_region = df.groupby(['Region'])['Units'].sum().reset_index()
value = unit_region['Units'].unique()

plt.plot(region,value)
plt.ylabel('jumlah unit terjual')
plt.xlabel('nama region')
plt.title('grafik penjualan per region')
plt.show()