import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# загрузка датафрейма в переменную
df = pd.read_csv('Data/crypto_data_updated_13_november.csv')

df['Date'] = pd.to_numeric(pd.to_datetime(df['Date']))

corr = df['Close (BTC)'].corr(df['Date'])
print("Корреляция между ценой и датой: ", corr)


df['Date'] = pd.to_datetime(df['Date'])
# построение графика рассеяния
plt.scatter(df['Date'], df['Close (BTC)'])

# добавление подписей осей и заголовка
plt.xlabel('Date (numeric)')
plt.ylabel('Price')
plt.title('Scatter plot of price vs date')

# вывод графика
#plt.show()
corr_matrix = df.corr()
fig, ax = plt.subplots(figsize=(10, 10))
# построение тепловой диаграммы
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Корреляция между ценой и датой")
plt.show()