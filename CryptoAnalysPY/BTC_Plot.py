import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc
import numpy as np
import datetime as dt
df = pd.read_csv('Data/crypto_data_updated_13_november.csv')

df['Date'] = pd.to_datetime(df['Date'])


df_filtered = df[(df['Date'].dt.year == 2018)]

plt.plot(df_filtered['Date'], df_filtered['Volume (ETH)'], color = 'b')
plt.tick_params(axis='x', labelsize=8)

plt.xlabel('Дата')
plt.ylabel('Цена')
plt.title('Volume эфира 2018')

plt.show()



#df_filtered = df[(df['Date'].dt.month >=2) & (df['Date'].dt.month <=4) & (df['Date'].dt.year == 2022) ]
#print(df_filtered)
# plt.plot(df_filtered['Date'], df_filtered['Close (BTC)'], 'r')
# plt.tick_params(axis='x', labelsize=8)
# plt.xlabel('Дата')
# plt.ylabel('Цена')
# plt.title('Цена биткоина с Февраля по Апрель')
# plt.axvline(x=dt.date(2022, 3, 1), color='b')
# plt.show()








#price.set_index('Date')
#selected_rows = price.loc[(price['Date'].dt.month == 2) & (price['Date'].dt.month == 3)]

#pd_filter = price['Date']#.isin (['2018-01-01 00:00:00+00:00'])
#pd_filter = price['Close (BTC)'].isin (['6635.750000'])
#print(pd_filter)
#plt.plot(price['Date'], price['Close (BTC)'], 'r')
#plt.xlabel('Дата')
#plt.ylabel('Цена')
#plt.title('Цена биткоина в промежутке 2017-2022')
#plt.show()