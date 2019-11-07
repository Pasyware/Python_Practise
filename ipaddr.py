# -*- coding: utf-8 -*-
import urllib.error, urllib.request, urllib.parse
import pymysql
import json
def url_open(url):
    headers=("user-agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data

conn = pymysql.connect(host='192.168.3.177',port=3307,user='root',password='123456',db='广州蜜罐2月',charset='utf8')
f1 = open(r"C:\Users\PQ\Desktop\temp\temp.txt",encoding="utf8")
line = f1.readline()
count=0
while(line):
    count=count+1
    if count <250:
        print(count)
        line=f1.readline()
        continue
    ip=line.rstrip('\n')
    #url="http://freeapi.ipip.net/"+ip
    #url="http://ip.taobao.com/service/getIpInfo.php?ip="+ip
    url="https://api.ttt.sh/ip/qqwry/"+ip+"?type=addr"
    resp=url_open(url)
    #print(resp)
    resp=resp.rstrip('\n')
    #dict1=json.loads(resp)
    #sql="update honeypot_all_ippos set pos2='"+ dict1['data']['country']+"."+dict1['data']['area']+"."+dict1['data']['region']+"."+dict1['data']['city']+"."+dict1['data']['isp']+"' where client_addr = '"+ip+"'"
    sql = "update honeypot_all_ippos set pos2='"+resp+"' where client_addr='" + ip + "'"
    conn.query(sql)
    conn.commit()
    print(count)
    print(sql)
    #if count==3:
    #    break
    line=f1.readline()
conn.close()
