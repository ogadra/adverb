# import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

rate = pd.read_csv('result-rate.csv', header=0, index_col=0, dtype='object')
rate = rate.T
rate[:] = rate[:].astype(float)

rate['year'] = list(range(1972,2008,5))


for col, target in rate.iteritems():
    # plt.plot(rate.year, target)

    lr = LinearRegression()
    Y = target.values
    try:
        X = rate.year.values.reshape(-1, 1)
        lr.fit(X,Y)
        print(col, lr.score(X,Y))
    except ValueError:
        # 1970-1974が欠損値となっている単語の計算
        X = rate.year[1:].values.reshape(-1, 1)
        Y = target[1:].values
        lr.fit(X,Y)
        print(col, lr.score(X,Y))
        pass

# plt.plot(rate.year,lr.predict(X), color='red')
# plt.show()