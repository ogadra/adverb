import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

rate = pd.read_csv('result-rate.csv', header=0, index_col=0, dtype='object')
rate = rate.T
rate[:] = rate[:].astype(float)

rate['year'] = list(range(1972,2008,5))

def regressionCalc(x, y, col):
    lr.fit(x,y)
    print(col)
    print('係数 =', lr.coef_[0]) # 説明変数の係数を出力
    print('切片 =', lr.intercept_) # 切片を出力
    print('決定係数 =', lr.score(X,Y))
    print('------------------------------------')
    return True

for col, target in rate.iteritems():
    if col == 'year':
        continue

    lr = LinearRegression()
    Y = target.values
    try:
        X = rate.year.values.reshape(-1, 1)
        regressionCalc(X, Y, col)
    except ValueError:
        # 1970-1974が欠損値となっている単語の計算
        X = rate.year[1:].values.reshape(-1, 1)
        Y = target[1:].values
        regressionCalc(X, Y, col)
