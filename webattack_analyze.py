import pymysql

conn=pymysql.connect(host='192.168.3.175',user='root',password='123456',db='vnap_data',charset='utf8')
cur = conn.cursor()
sql1="select client_addr,server_addr,count(*) from webattack3 group by client_addr,server_addr having count(*) < 10 ORDER BY count(*)"
sql2= "SELECT start_time,method,url,client_addr,client_biz_group,server_addr,server_biz_group,details FROM `webattack3` "
count = 0
try:
    cur.execute(sql1)
    result1 = cur.fetchall()
    len1=len(result1)
    i = 0
    while ( i<len1 ):
        client_addr=result1[i][0]
        server_addr=result1[i][1]
        condition="where client_addr='"+client_addr+"' and server_addr='"+server_addr+"' and url not like '%CREATEDTIME>to_char%' and url not like '%IF(ISNULL(IFNULL(%'"
        sql3=sql2+condition
        i=i+1
        cur.execute(sql3)
        result2 = cur.fetchall()
        print("########################################################################################################################################3")
        for row in result2:
            count = count +1
            print("Count:"+str(count))
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])


except Exception as e:
    raise e
finally:
    conn.close()