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
print('係数 =', lr.coef_[0]) # 説明変数の係数を出力
print('切片 =', lr.intercept_) # 切片を出力
print('決定係数R^2 =', lr.score(X,Y))


# plt.plot(rate.year,lr.predict(X), color='red')
# plt.show()