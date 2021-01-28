import matplotlib.pyplot as plt
import pandas as pd
import json

rate = pd.read_csv('result-rate.csv', header=0, index_col=0, dtype='object')
rate = rate.T

rate[:] = rate[:].astype(float)


plt.rcParams['font.family'] = 'Noto Sans CJK JP'
plt.rcParams["font.size"] = 18
rate.plot(subplots=True, sharex=True, sharey=True, layout=(6,2), figsize=(15,20))

plt.savefig('imgs/graph.png')