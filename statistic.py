# coding:utf-8
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
import os
import test_datetime as DT
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['figure.figsize'] = (12.0, 8.0)

data=[]
with open(r"C:\Users\PQ\Desktop\temp\temp.txt") as f1:
    for line in f1:
        line=line.rstrip("\n")
        date,num=line.partition('\t')[::2]
        #print(date+"    "+num)
        data.append((DT.test_datetime.strptime(date, "%Y-%m-%d"), num))

x = [date2num(date) for (date, value) in data]
y = [int(value) for (date, value) in data]

#print(x)
#print(y)

fig = plt.figure()
graph = fig.add_subplot(111)
graph.set_title('探测扫描IP数的时间分布')
graph.set_xlabel('日期')
graph.set_ylabel('IP数')
# Plot the data as a red line with round markers
graph.plot(x,y)

graph.set_xticks(x)
graph.set_xticklabels(
    [date.strftime("%Y-%m-%d") for (date,value) in data], rotation=45
)
graph.set_yticks(y)
graph.set_yticklabels(
    [value for (date,value) in data]
)
plt.grid(True)
#plt.xticks(x[::8])
# print [x[f_value] for f_value in range(0, len(x), 8)]
plt.show()
