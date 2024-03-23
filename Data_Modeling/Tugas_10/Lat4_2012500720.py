import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("officesuppliesnew.csv")
df = df.groupby(['Item'])['Units'].sum().reset_index()
df = df.loc[0:,['Item','Units']]
df = df.set_index(['Item'])
df.plot(color='Blue')

plt.title('grafik penjualan per pegawai')
plt.ylabel('jumlah unit terjual')
plt.xlabel('nama itemexit')
plt.show()