#coding=utf-8
#爬取taobao商品
import urllib.error, urllib.request, urllib.parse
import http.cookiejar
#import pymysql
import re
import time
import datetime
import xlwt
from tkinter import *
from tkinter import filedialog

#打开网页，获取网页内容
def url_open(url):
    headers=("user-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data
'''
    cookie_filename = 'cookie_tb'
    cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie_aff)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(url)
    try:
        response = opener.open(request).read().decode("utf-8","ignore")
        return response
    except urllib.error.URLError as e:
        print(e.reason)
        return
'''

'''
#将数据存入mysql中
def data_Import(sql):
    conn=pymysql.connect(host='192.168.3.175',user='root',password='123456',db='taobao',charset='utf8')
    conn.query(sql)
    conn.commit()
    conn.close()
'''

def selectPath():
    path_ = filedialog.askopenfilename()
    path.set(path_)

def show_process(text,string):
    text.insert(END,string)
    text.see(END)
    text.update()

def clear_process(text):
    text.delete(0.0, END)
    text.update()

def num_check(str,text):
    try:
        return int(str)
    except:
        text.insert(END, '########################\n    请输入数字！！\n########################\n')
        text.see(END)
        text.update()
        return 0

def search_stop():
    global sign_stop
    sign_stop = 1

def search_tb(path,page,num,text):
    global lock1
    global sign_stop
    if lock1 == 1:
        return
    else:
        lock1 = 1
    if sign_stop == 1:
       sign_stop = 0
    if path == "":
        show_process(text,"[Errno 1]输入文件为空\n")
        return
    if page == "" or num_check(page,text) < 1 or num_check(page,text) >100:
        show_process(text, "[Errno 1] 输入页数有误\n")
        return
    if num == "" or num_check(num,text) < 1 or num_check(num,text) >44:
        show_process(text, "[Errno 1] 输入个数有误\n")
        return
    try:
        if sign_stop == 1:
            lock1 = 0
            sign_stop = 0
            clear_process(text)
            return
        today_date=datetime.datetime.today().strftime("%Y-%m-%d_%H%M%S")
        show_process(text,"Open file:"+path+"\n")
        with open(path, 'r', encoding='utf-8') as file:
          list = file.readlines()
        count=0
        excel1=xlwt.Workbook()
        sheet1=excel1.add_sheet('商品表',cell_overwrite_ok=True)
        sheet1.col(0).width = 2000
        sheet1.col(1).width = 15000
        sheet1.col(2).width = 2000
        sheet1.col(3).width = 1500
        sheet1.col(4).width = 3000
        sheet1.col(5).width = 5000
        sheet1.col(6).width = 2000
        sheet1.col(7).width = 3000
        sheet1.col(8).width = 36000

        #样式组件
        alignment1 = xlwt.Alignment()
        alignment1.horz = 0x01
        alignment1.vert = 0x00
        border1 = xlwt.Borders()
        border1.left = xlwt.Borders.THICK
        border1.right = xlwt.Borders.THICK
        border1.top = xlwt.Borders.THICK
        border1.bottom = xlwt.Borders.THICK
        border1.left_colour = 0x3A
        border1.right_colour = 0x3A
        border1.top_colour = 0x3A
        border1.bottom_colour = 0x3A
        pattern1=xlwt.Pattern()
        pattern1.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern1.pattern_fore_colour = 3  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
        pattern2 = xlwt.Pattern()
        pattern2.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern2.pattern_fore_colour = 22
        font1=xlwt.Font()
        font1.name = u'宋体'
        font2=xlwt.Font()
        font2.name = u'微软雅黑'
        font2.bold=True
        font2.colour_index =0x50
        #样式配置
        style1 = xlwt.XFStyle()
        style1.border=border1
        style1.alignment=alignment1
        style1.font=font1
        style2 = xlwt.XFStyle()
        style2.border=border1
        style2.alignment=alignment1
        style2.font = font2
        style2.pattern = pattern1
        style3 = xlwt.XFStyle()
        style3.border = border1
        style3.alignment = alignment1
        style3.font = font2
        style3.pattern = pattern2
        #标题
        sheet1.write(count, 0, "ID", style2)
        sheet1.write(count, 1, "商品名称", style2)
        sheet1.write(count, 2, "价格", style2)
        sheet1.write(count, 3, "运费", style2)
        sheet1.write(count, 4, "销量", style2)
        sheet1.write(count, 5, "商铺", style2)
        sheet1.write(count, 6, "评论数", style2)
        sheet1.write(count, 7, "城市", style2)
        sheet1.write(count, 8, "图片链接", style2)
        count = count + 1
        for p in range(0, len(list)):
          list[p] = list[p].rstrip('\n')
          if list[p] == "":
              continue
          print(list[p])
          show_process(text,"正在查询："+list[p]+"\n")
          flag = 0
          while ( flag == 0 ):
           # 定义要查询的商品关键词
           sheet1.write(count,0,str(count),style1)
           sheet1.write_merge(count,count,1,8,"【"+str(p+1)+"】"+list[p], style3)
           count = count + 1
           keywords = urllib.request.quote(list[p])
           print(keywords)
           # 定义要爬取的页数
           for i in range(int(page)):
              if sign_stop == 1:
                  lock1 = 0
                  sign_stop = 0
                  clear_process(text)
                  return
              url ="https://list.tmall.com/search_product.htm?q="+keywords+"&type=p&vmarket=&spm=a211oj.0.a2227oh.d100&from=..pc_1_searchbutton"
              #url ="https://s.taobao.com/search?q="+ keywords +"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190226&ie=utf8"
              #url ="https://s.taobao.com/search?q="+ keywords + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s="+ str(i * 44)
              #url = "https://s.taobao.com/search?q=" + keywords + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=" + str(i * 44)
              #url = "https://s.taobao.com/search?q="+ keywords +"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190304&ie=utf8"
              #url = "https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20170905&stats_click=search_radio_all%3A1&js=1&imgfile=&q="+keywords+"&suggest=0_1&_input_charset=utf-8&wq=u&suggest_query=u&source=suggest&p4ppushleft=5%2C48&s="+ str(i * 44)
              data = url_open(url)
              print(url)
              # 定义各个字段正则匹配规则
              img_pat = '"pic_url":"(//.*?)"'
              name_pat = '"raw_title":"(.*?)"'
              nick_pat = '"nick":"(.*?)"'
              price_pat = '"view_price":"(.*?)"'
              fee_pat = '"view_fee":"(.*?)"'
              sales_pat = '"view_sales":"(.*?)"'
              comment_pat = '"comment_count":"(.*?)"'
              city_pat = '"item_loc":"(.*?)"'
              #detail_url_pat = 'detail_url":"(.*?)"'
              # 查找满足匹配规则的内容，并存在列表中
              imgL = re.compile(img_pat).findall(data)
              nameL = re.compile(name_pat).findall(data)
              nickL = re.compile(nick_pat).findall(data)
              priceL = re.compile(price_pat).findall(data)
              feeL = re.compile(fee_pat).findall(data)
              salesL = re.compile(sales_pat).findall(data)
              commentL = re.compile(comment_pat).findall(data)
              cityL = re.compile(city_pat).findall(data)
              #detail_urlL = re.compile(detail_url_pat).findall(data)
              # print('正在爬取第' + str(i+1) + "页，第" + str(j) + "个商品信息...")
              show_process(text, "  正在爬取第" + str(i + 1) + "页的"+str(int(num))+"个商品信息...\n")
              if len(imgL) > 0:
                  flag = 1
                  continue
              for j in range(len(imgL)):
                  if sign_stop == 1:
                      lock1 = 0
                      sign_stop = 0
                      clear_process(text)
                      return
                  if j > int(num):
                      continue
                  img = "http:" + imgL[j]  # 商品图片链接
                  name = nameL[j]  # 商品名称
                  nick = nickL[j]  # 淘宝店铺名称
                  price = priceL[j]  # 商品价格
                  fee = feeL[j]  # 运费
                  sales = salesL[j]  # 商品付款人数
                  comment = commentL[j]  # 商品评论数，会存在为空值的情况
                  if (comment == ""):
                      comment = 0
                  city = cityL[j]  # 店铺所在城市
                  #detail_url = detail_urlL[j]  # 商品链接
                  # sql = "insert into list2(name,price,fee,sales,comment,city,nick,img,detail_url) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (name, price, fee, sales, comment, city, nick, img, detail_url)
                  # data_Import(sql)
                  sheet1.write(count, 0, str(count),style1)
                  sheet1.write(count, 1, name, style1)
                  sheet1.write(count, 2, price, style1)
                  sheet1.write(count, 3, fee, style1)
                  sheet1.write(count, 4, sales, style1)
                  sheet1.write(count, 5, nick, style1)
                  sheet1.write(count, 6, comment, style1)
                  sheet1.write(count, 7, city, style1)
                  sheet1.write(count, 8, img, style1)
                  count = count + 1
                  time.sleep(0.2)
              # print("爬取完成，且数据已存入数据库")
              show_process(text, "  该页爬取完成，数据已存入Excel缓存\n")
              percent=round(float((p+1)*100/len(list)),2)
              show_process(text, "检索进度："+str(percent)+"%\n")
        save_path="商品信息"+today_date+".xls"
        excel1.save(save_path)
        #excel1.save('Commodity.xls')
        show_process(text, "#############################################\n# 导出  "+save_path+"  成功 #\n#############################################\n")
        lock1 = 0
    except Exception as e:
        #print(str(e))
        show_process(text,str(e)+'\n')

if __name__=='__main__':
    lock1 = 0
    sign_stop = 0

    top = Tk()
    top.title("自动爬取商品信息")
    top.geometry("450x300")
    #源表单文件
    path = StringVar()
    lab1=Label(top, text="查询表单:")
    lab1.grid(row=0, column=0)
    lab1.place(x=10,y=10,width=50,height=30)
    text1 = Entry(top, textvariable=path)
    text1.grid(row=0, column=1)
    text1.place(x=70, y=10,width=300,height=30)
    bt1=Button(top, text="文件选择", command=selectPath)
    bt1.grid(row=0, column=2)
    bt1.place(x=380,y=10,width=60,height=30)

    text4=Text(top)
    text4.place(x=10,y=90,width=410,height=200)
    scroll1=Scrollbar(top)
    scroll1.place(x=420,y=90,width=20,height=200)
    scroll1.config(command=text4.yview)
    text4.config(yscrollcommand=scroll1.set)

    page = StringVar()
    num = StringVar()
    lab2 = Label(top, text="查询页数:")
    lab2.place(x=10, y=50, width=50, height=30)
    text2 = Entry(top, textvariable=page)
    page.set("1")
    text2.place(x=70, y=50, width=30, height=30)
    lab3 = Label(top, text="每页个数:")
    lab3.place(x=120, y=50, width=50, height=30)
    text3 = Entry(top, textvariable=num)
    num.set("12")
    text3.place(x=180, y=50, width=30, height=30)
    bt2=Button(top,text="一键爬取并导出",command=lambda:search_tb(path.get(),page.get(),num.get(),text4))
    bt2.place(x=230,y=50,width=100,height=30)
    bt3=Button(top,text="终止检索",command=search_stop)
    bt3.place(x=350,y=50,width=60,height=30)

    # 进入消息循环
    top.mainloop()

