import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

data = pd.read_csv('bitcoin_data.csv')
input('Data read completed. Press enter key to continue: ')
data = data.dropna()
data['Time'] = data['Timestamp'].apply(lambda x: pd.to_datetime(datetime.fromtimestamp(x)))
data = data.set_index(data['Time'])
plt.plot(data[['Close', 'Time']])

# checking stationarity of the time series data
