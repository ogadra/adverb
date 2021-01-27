import matplotlib.pyplot as plt
import pandas
import json

with open('./result.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

fig = plt.figure()
ax = fig.add_subplot(111)


for i in range(1,len(data),2):
    rate = []
    for j in range(2,len(data[i])):
        try:
            rate.append(int(data[i][j]) / (int(data[i][j]) + int(data[i+1][j])))
        except ZeroDivisionError:
            if len(rate) == 0:
                pass
            else:
                rate.append('')
    if i == 1:
        break

ax.plot(rate.dropna(how='any'))
ax.legend()
