import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import pandas as pd
from datetime import datetime
rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('bitcoin_price.csv')
data = data.dropna()
data = data.set_index(data['Date'])
data.index = data.index.to_datetime()
print("Length of data =", len(data))
close_values = data['Close']

# checking stationarity of the time series data
original = plt.plot(close_values, color='blue', label='Original')
moving_avg = pd.rolling_mean(close_values, window=50)
mean = plt.plot(moving_avg, color='red', label='Moving Average')
plt.legend(loc='best')
plt.title('Moving Average vs Original values over time')
plt.show()

# seasonality stuff (differencing the model)
data_diff = abs(moving_avg - moving_avg.shift())
plt.plot(data_diff)
plt.show()