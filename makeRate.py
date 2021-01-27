import csv
import json

with open('./result.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

for i in range(len(data)):
    data[i][2:] = [int(i) for i in data[i][2:]]

rate = [['副詞']]
rate[0].extend([str(i) + '-' + str(i+4) for i in range(1970,2006,5)])
for i in range(1,len(data),2):
    rateChild = [data[i][0]]
    for j in range(2,(len(data[i])-2)//5+2):
        molecular = sum(data[i][(j-2)*5+2:(j-1)*5+2])
        denominator = sum(data[i+1][(j-2)*5+2:(j-1)*5+2]) + molecular

        try:
            rateChild.append(molecular / denominator)
        except ZeroDivisionError:
            rateChild.append('')
    rate.append(rateChild)

with open('result-rate.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rate)