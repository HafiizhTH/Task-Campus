import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("officesuppliesnew.csv")
region = df['Rep'].unique()
region.sort()

unit_region = df.groupby(['Rep'])['Units'].sum().reset_index()
value = unit_region['Units'].unique()

plt.plot(region,value)
plt.ylabel('jumlah unit terjual')
plt.xlabel('nama pegawai')
plt.title('grafik penjualan per pegawai')
plt.show()