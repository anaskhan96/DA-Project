import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import pandas as pd
from datetime import datetime
#rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('bitcoin_price.csv')
data = data.dropna()
data = data[::-1]
print("Length of data =", len(data))
test_data = data.tail(500)
data = data.set_index(['Date'])
data.index = data.index.to_datetime()
alpha_vals = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
mse = []

# checking stationarity of the time series data
for alpha in alpha_vals:
    plt.plot(data['Close'], color='blue', label='Original')
    ses = pd.ewma(data['Close'], com = 1/alpha-1)
    ses_test = ses.tail(500)
    mse.append(sum([(x - y)**2 for x, y in zip(ses_test, test_data['Close'])])/500)
    print("Predicted value for next day: ", (ses.tail(1) + alpha * (data.tail(1)['Close'] - ses.tail(1))))
    plt.plot(ses, color='red', label='Exponential Smoothing')
    plt.legend(loc='best')
    plt.title('Exponential Smoothing with alpha = {0} vs Original values over time'.format(alpha))
    plt.show()

print(mse)