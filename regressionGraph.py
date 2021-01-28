# import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

rate = pd.read_csv('result-rate.csv', header=0, index_col=0, dtype='object')
rate = rate.T
rate[:] = rate[:].astype(float)

rate['year'] = list(range(1972,2008,5))
target = rate['ゼンゼン']

lr = LinearRegression()
Y = target.values
X = rate.year.values.reshape(-1, 1)
lr.fit(X,Y)

fig = plt.figure(figsize=(9.6,5.4))
ax = fig.add_subplot(111, ylim=(0.0, 1.0))
# print(col, lr.score(X,Y))
ax.plot(rate.year, target)
ax.plot(rate.year,lr.predict(X), color='red')

fig.savefig('./imgs/regression.png')