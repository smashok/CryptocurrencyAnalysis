import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/crypto_data_updated_13_november.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.plot(x= 'Date', y = ['Volume (BTC)',
                        'Volume (ETH)',
                        'Volume (USDT)',
                        'Volume (BNB)'] )
plt.show()