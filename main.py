import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import pandas as pd
from datetime import datetime
rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('bitcoin_data_time.csv')
data = data.dropna()
data = data.set_index(data['Timestamp'])
data.index = data.index.to_datetime()
data.index = pd.to_datetime(data.index, format='%Y')
data = data.resample('44000Min')
print("Length of data =", len(data))
close_values = data['Close']

# checking stationarity of the time series data
original = plt.plot(close_values, color='blue', label='Original')
rolmean = pd.rolling_mean(close_values, window=12)
mean = plt.plot(rolmean, color='red', label='Moving Average')
plt.legend(loc='best')
plt.title('Moving Average vs Original values over time')
plt.show()