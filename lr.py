import numpy as np
import pandas as pd

df = pd.read_csv('bitcoin_price.csv')
df= df.drop('Date',1)
p = df.loc[df['Close'].idxmax()]
print (p)

from sklearn.preprocessing import MinMaxScaler
cols = df.columns.values
print (cols)

Min_max_scaler = MinMaxScaler()
df[cols] = Min_max_scaler.fit_transform(df[cols])

X = df.drop('Weighted_Price',1).values
y = df['Weighted_Price']

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(X_train,y_train)

print ('Residual sum of squares Train: %.2f' % np.mean((model.predict(X_train)- y_train) ** 2))
print ('Residual sum of squares Test: %.2f' % np.mean((model.predict(X_test)- y_test) ** 2))
