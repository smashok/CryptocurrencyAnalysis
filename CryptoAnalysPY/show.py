import pandas as pd
pd.options.display.max_columns = None
pd.set_option('display.width', 150)
df = pd.read_csv('Data/crypto_data_updated_13_november.csv')
#df.head(10)
print(df.head(10))