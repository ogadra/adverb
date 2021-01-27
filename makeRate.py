import csv
import json

with open('./result.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

rate = list()
for i in range(1,len(data),2):
    rateChild = [data[i][0]]
    for j in range(2,len(data[i])):
        try:
            rateChild.append(int(data[i][j]) / (int(data[i][j]) + int(data[i+1][j])))
        except ZeroDivisionError:
            rateChild.append('')
    rate.append(rateChild)

with open('result-rate.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rate)