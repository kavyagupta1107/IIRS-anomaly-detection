import os
import pandas as pd
import numpy as np
from sklearn import preprocessing
import seaborn as sns
sns.set(color_codes=True)
import matplotlib.pyplot as plt
%matplotlib inline

from numpy.random import seed
from tensorflow import set_random_seed


df = pd.read_csv('index_data.csv')
df = df[['date_time', 'value']]
df.info()
df['value'].describe()
df.plot(x='date_time', y='value', figsize=(12,6))
plt.xlabel('Date time')
plt.ylabel('index value')
plt.title('Time Series of Index value for a selected lat/long');


data = df[['price_usd', 'value']]
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# train isolation forest
#outliers_fraction=0.01
model =  IsolationForest(contamination=outliers_fraction)
model.fit(data) 
df['anomaly2'] = pd.Series(model.predict(data))

# visualization
fig, ax = plt.subplots(figsize=(10,6))
#entries corresponding to anomaly2=-1 are anomalies
a = df.loc[df['anomaly2'] == -1, ['date_time', 'value']] #anomaly

ax.plot(df['date_time'], df['value'], color='blue', label = 'Normal')
ax.scatter(a['date_time'],a['value'], color='red', label = 'Anomaly')
plt.legend()
plt.show();