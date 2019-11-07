# -*- coding: utf-8 -*-

#f = open(r"C:\Users\PQ\PycharmProjects\py-webscanner\all.txt" , encoding='utf8')  # 返回一个文件对象
f = open (r"C:\Users\PQ\PycharmProjects\crawler\data.json" , encoding='utf8')
#f1 = open(r"C:\Users\PQ\PycharmProjects\py-webscanner\4part.txt" , "w",encoding='utf8')
line = f.readline()
count=0
while(line):
    count = count +1
    print("【"+str(count)+"】\n")
    #f1.write(line)
    #if count==2000:
    #    break
    line = f.readline()