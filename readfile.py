# -*- coding: utf-8 -*-
import pymysql

num = 1
while ( num < 9):
 f = open("F:\开发中\流量检测Web攻击\现场测试数据\web"+str(num),encoding='utf8')     # 返回一个文件对象
 line = f.readline()             # 调用文件的 readline()方法
 count = 0
 conn=pymysql.connect(host='192.168.3.175',user='root',password='123456',db='vnap_data',charset='utf8')
 while line:
    count = count + 1
    #if count == 20:
    #   break
    line = line.rstrip('\n')
    start_time = line.split('\t')[0]
    start_time_nano = line.split('\t')[1]
    end_time = line.split('\t')[2]
    end_time_nano = line.split('\t')[3]
    error_code = line.split('\t')[4]
    error_msg = line.split('\t')[5]
    method = line.split('\t')[6]
    host = line.split('\t')[7]
    url = line.split('\t')[8]
    domain_name = line.split('\t')[9]
    referer = line.split('\t')[10]
    user_agent = line.split('\t')[11]
    server = line.split('\t')[12]
    content_type = line.split('\t')[13]
    client_addr = line.split('\t')[14]
    client_addr_value = line.split('\t')[15]
    client_port = line.split('\t')[16]
    server_addr = line.split('\t')[17]
    server_addr_value = line.split('\t')[18]
    server_port = line.split('\t')[19]
    uplink_pkts = line.split('\t')[20]
    uplink_octets = line.split('\t')[21]
    downlink_pkts = line.split('\t')[22]
    downlink_octets = line.split('\t')[23]
    os_name = line.split('\t')[24]
    os_category = line.split('\t')[25]
    browser_name = line.split('\t')[26]
    browser_category = line.split('\t')[27]
    app_desc = line.split('\t')[28]
    cat1_desc = line.split('\t')[29]
    client_biz_group = line.split('\t')[30]
    server_biz_group = line.split('\t')[31]
    x_forwarded_for = line.split('\t')[32]
    pattern = line.split('\t')[33]
    details = line.split('\t')[34]
    scanner = line.split('\t')[35]

    sql="INSERT INTO vnap_data.webattack(start_time,start_time_nano,end_time,end_time_nano,error_code,error_msg,method,host,url,domain_name,referer,user_agent,server,content_type,client_addr,client_addr_value,client_port,server_addr,server_addr_value,server_port,uplink_pkts,uplink_octets,downlink_pkts,downlink_octets,os_name,os_category,browser_name,browser_category,app_desc,cat1_desc,client_biz_group,server_biz_group,x_forwarded_for,pattern,details,scanner)\
    VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
    %(start_time,start_time_nano,end_time,end_time_nano,error_code,error_msg,method,host,url,domain_name,referer,user_agent,server,content_type,client_addr,client_addr_value,client_port,server_addr,server_addr_value,server_port,uplink_pkts,uplink_octets,downlink_pkts,downlink_octets,os_name,os_category,browser_name,browser_category,app_desc,cat1_desc,client_biz_group,server_biz_group,x_forwarded_for,pattern,details,scanner)

    print(sql)
    conn.query(sql)
    conn.commit()
    print("Web[ "+str(num)+" ]Insert[ "+str(count)+" ]")
    line = f.readline()
 num = num + 1
conn.close()
f.close()
