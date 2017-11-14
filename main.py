import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

data = pd.read_csv('bitcoin_data_time.csv')
data = data.dropna()
data = data.set_index(data['Time'])

# checking stationarity of the time series data
plt.plot(data['Close'])
plt.show()
