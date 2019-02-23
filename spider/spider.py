# -*- coding:utf-8 -*-
import urllib.request
import json
import os
import sys
import pymysql
import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import urllib.parse
from PyQt5.QtCore import QCoreApplication
import time
import sys
import numpy
from pyecharts import Bar
from pyecharts import Geo
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# https://s.taobao.com/api?m=customized&q=%E5%88%9D%E9%9F%B3%E6%9C%AA%E6%9D%A5&cat=50016564&s=0
# https://s.taobao.com/search?q=%E5%88%9D%E9%9F%B3%E6%9C%AA%E6%9D%A5&cat=50016564&s=0
class util_urlencode:
    def __init__(self, str):
        self.str = str

    def encode(self):
        return urllib.parse.urlencode({"q" : self.str})

class get_user_agent:
    def __init__(self):
        self.ua_list = ["Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
        "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
        "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
        "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"
        ]

    def get(self):
        ua = random.choice(self.ua_list)
        return ua

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 596)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../kirito.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.creditDesc = QtWidgets.QRadioButton(Form)
        self.creditDesc.setGeometry(QtCore.QRect(540, 350, 115, 19))
        self.creditDesc.setObjectName("creditDesc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.saleDesc = QtWidgets.QRadioButton(Form)
        self.saleDesc.setGeometry(QtCore.QRect(410, 350, 115, 19))
        self.saleDesc.setObjectName("saleDesc")
        self.search_num = QtWidgets.QSpinBox(Form)
        self.search_num.setGeometry(QtCore.QRect(140, 290, 151, 31))
        self.search_num.setMaximum(100000000)
        self.search_num.setObjectName("search_num")
        self.search_name = QtWidgets.QTextEdit(Form)
        self.search_name.setGeometry(QtCore.QRect(140, 240, 251, 31))
        self.search_name.setObjectName("search_name")
        self.priceAsc = QtWidgets.QRadioButton(Form)
        self.priceAsc.setGeometry(QtCore.QRect(140, 390, 115, 19))
        self.priceAsc.setObjectName("priceAsc")
        self.renqiDesc = QtWidgets.QRadioButton(Form)
        self.renqiDesc.setGeometry(QtCore.QRect(270, 350, 115, 19))
        self.renqiDesc.setObjectName("renqiDesc")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.priceDesc = QtWidgets.QRadioButton(Form)
        self.priceDesc.setGeometry(QtCore.QRect(270, 390, 115, 19))
        self.priceDesc.setObjectName("priceDesc")
        self.totalAsc = QtWidgets.QRadioButton(Form)
        self.totalAsc.setGeometry(QtCore.QRect(410, 390, 115, 19))
        self.totalAsc.setObjectName("totalAsc")
        self.default_2 = QtWidgets.QRadioButton(Form)
        self.default_2.setGeometry(QtCore.QRect(140, 350, 115, 19))
        self.default_2.setObjectName("default_2")
        self.totalDesc = QtWidgets.QRadioButton(Form)
        self.totalDesc.setGeometry(QtCore.QRect(540, 390, 115, 19))
        self.totalDesc.setObjectName("totalDesc")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 520, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 430, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.use_db = QtWidgets.QTextEdit(Form)
        self.use_db.setGeometry(QtCore.QRect(140, 430, 251, 31))
        self.use_db.setObjectName("use_db")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 470, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(650, 160, 241, 401))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../miku.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(170, 60, 571, 101))
        font = QtGui.QFont()
        font.setFamily("梦幻花园体")
        font.setPointSize(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.progress = QtWidgets.QLabel(Form)
        self.progress.setGeometry(QtCore.QRect(30, 530, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progress.setFont(font)
        self.progress.setText("")
        self.progress.setObjectName("progress")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.submit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "淘宝信息采集器    BY：暴走的carry"))
        self.label_2.setText(_translate("Form", "最大数量："))
        self.creditDesc.setText(_translate("Form", "信用"))
        self.label.setText(_translate("Form", "商品名："))
        self.saleDesc.setText(_translate("Form", "销量"))
        self.priceAsc.setText(_translate("Form", "价格低到高"))
        self.renqiDesc.setText(_translate("Form", "人气"))
        self.label_3.setText(_translate("Form", "排序方式："))
        self.priceDesc.setText(_translate("Form", "价格高到低"))
        self.totalAsc.setText(_translate("Form", "总价格低到高"))
        self.default_2.setText(_translate("Form", "综合排序"))
        self.totalDesc.setText(_translate("Form", "总价格高到低"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.label_4.setText(_translate("Form", "数据库名："))
        self.label_5.setText(_translate("Form", "为空则不保存到数据库"))
        self.label_7.setText(_translate("Form", "淘宝信息采集器"))

class pymysql_util:
    def __init__(self, host, user, password, port ,database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def open(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database,
                charset="utf8"
            )
            self.cursor = self.conn.cursor()
        except Exception as e :
            print(e)


    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, sql, params):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)

    def r(self, sql, params):   # 查询
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)

    def creat_new_table(self, table_name):
        try:
            self.open()
            sql = "CREATE TABLE IF NOT EXISTS " + table_name + "(`id` INT(20) UNSIGNED AUTO_INCREMENT,`raw_title` VARCHAR(255) ,`detail_url` VARCHAR(255) ,`view_price` VARCHAR(255) ,`view_fee` VARCHAR(255) ,`item_loc` VARCHAR(255) ,`view_sales` VARCHAR(255) ,`comment_count` VARCHAR(255) ,`nick` VARCHAR(255) ,PRIMARY KEY ( `id` ))"
            self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)

class mikuGK_spider:
    def __init__(self, search_name, search_type, mywindow):
        self.window = mywindow    # 将窗口对象传入
        self.search_name = search_name   # 需要搜索的商品名
        self.search_type = search_type   # 搜索方式
        self.url = "https://s.taobao.com/api?data-key=sort&m=customized&s="
        self.page = 0
        self.User_Agent = {
            "User-Agent" : get_user_agent().get()
        }
        self.raw_titles = []  # raw_title 标题
        self.detail_urls = []  # detail_url 详细页面地址
        self.view_prices = []  # view_price 价格
        self.view_fees = []  # view_fee 邮费
        self.item_locs = []  # item_loc 商品发货地
        self.view_saless = []  # view_sales 付款人数
        self.comment_counts = []  # comment_count 评论数
        self.nicks = []  # nick 卖家名称
        self.types = {
            "defalut": "默认",
            "renqi-desc": "人气",
            "sale-desc": "售价",
            "credit-desc": "信用",
            "price-asc": "价格由低到高",
            "price-desc": "价格由高到低",
            "total-asc": "总价格由低到高",
            "total-desc": "总价格由高到低"
        }
    def get_html(self):
        # 添加页码
        full_url = self.url + str(self.page) + "&"
        # 添加搜索商品名
        full_url += util_urlencode(self.search_name).encode() + "&"
        # 添加搜索方式
        full_url = full_url + "data-value=" + self.search_type
        # 发送请求
        request = urllib.request.Request(full_url, headers=self.User_Agent)
        # 接受响应
        respones = urllib.request.urlopen(request)
        html = respones.read().decode("utf-8") # 获取页面源代码
        self.save_full_data(html) # 将所有数据存入本地文件
        try:
            self.html_dict = json.loads(html)  # 将json字符串转换成python对象（字典）
        except:
            print("json error")
        self.html_len = len(html)  # 数据的长度

    # 将所有数据存入本地文件
    def save_full_data(self,html):
        path_data = "../data"
        if not os.path.exists(path_data):   # 如果没有data文件夹则创建一个
            os.mkdir(path_data)
        path = "../data/" + self.search_name + "_" + self.search_type
        if not os.path.exists(path):   # 如果路径不存在就创建文件夹
            os.mkdir(path)
        with open(path + "/%s~%s.json"%(self.page,self.page+12), mode="w",encoding="utf-8") as f:
            f.write(html)
            print("将所有数据存入本地文件")
            self.window.progress.setText("将所有数据存入本地文件")
            QtWidgets.QApplication.processEvents()    # 刷新页面
            time.sleep(0.5)

    # 获取一页的信息
    def get_one_page_message(self):
        self.get_html()   # 获取页面源代码
        raw_title = []   # raw_title 标题
        detail_url = []   # detail_url 详细页面地址
        view_price = []   # view_price 价格
        view_fee = []   # view_fee 邮费
        item_loc = []   # item_loc 商品发货地
        view_sales = []   # view_sales 付款人数
        comment_count = []   # comment_count 评论数
        nick = []     # nick 卖家名称
        try:
            for i in range(12):
                raw_title.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["raw_title"])
                detail_url.append("https://" + self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["detail_url"])
                view_price.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["view_price"])
                view_fee.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["view_fee"])
                item_loc.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["item_loc"])
                view_sales.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["view_sales"])
                comment_count.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["comment_count"])
                nick.append(self.html_dict["API.CustomizedApi"]["itemlist"]["auctions"][i]["nick"])

            self.raw_titles += raw_title
            self.detail_urls += detail_url
            self.view_prices += view_price
            self.view_fees += view_fee
            self.item_locs += item_loc
            self.view_saless += view_sales
            self.comment_counts += comment_count
            self.nicks += nick
        except:
            pass

    # 将数据存入数据库
    def save_in_mysql(self, db_name):
        m_utils = pymysql_util("localhost", "root", "root", 3306, db_name)
        # 以搜索名创建一张新表
        table_name = self.search_name + "_" + self.types[self.search_type]
        m_utils.creat_new_table(table_name)
        # 将信息打包
        zip_message = zip(self.raw_titles, self.detail_urls, self.view_prices, self.view_fees, self.item_locs,
                          self.view_saless, self.comment_counts, self.nicks)
        for each in zip_message:
            sql = "insert into " + table_name + "(raw_title,detail_url,view_price,view_fee,item_loc,view_sales,comment_count,nick) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            m_utils.insert(sql, each)
        print("将数据存入数据库")
        self.window.progress.setText("将数据存入数据库")
        QtWidgets.QApplication.processEvents()  # 刷新页面


class mikugk_location_chart:
    def __init__(self):
        self.types = {
            "defalut": "默认",
            "renqi-desc": "人气",
            "sale-desc": "售价",
            "credit-desc": "信用",
            "price-asc": "价格由低到高",
            "price-desc": "价格由高到低",
            "total-asc": "总价格由低到高",
            "total-desc": "总价格由高到低"
        }

    def get_location_bar(self, db_name, search_num, search_type, search_name):
        util = pymysql_util("localhost", "root", "root", 3306, db_name)
        table_name = search_name + "_" + self.types[search_type]   # 表名
        sql = "select item_loc from " + table_name
        print(sql)
        item_loc = util.r(sql, [])  # 查询
        item_loc_list = []
        for each in item_loc:
            item_loc_list.append(each[0])

        item_loc_dic = {}  # 字典类型 key:地址，value：数量
        for each in item_loc_list:  # 遍历数据库中所有的地址
            item_loc_keys = numpy.array(list(item_loc_dic.keys()))
            if not item_loc_keys.__contains__(each):  # 如果列表里不包含该地址，则添加
                item_loc_dic[each] = 1
            else:  # 如果存在则数量加一
                item_loc_dic[each] += 1

        item_loc_value_moreThan50 = {}  # 只存最大查询量的百分之一，字典类型 key:地址，value：数量
        for key, value in item_loc_dic.items():
            if value >= search_num/100:
                item_loc_value_moreThan50[key] = value

        item_loc_value_moreThan50_sort = sorted(item_loc_value_moreThan50.items(), key=lambda x: x[1], reverse=True)

        item_loc_value_moreThan50_sort_dic = {}
        for each in item_loc_value_moreThan50_sort:
            item_loc_value_moreThan50_sort_dic[each[0]] = each[1]

        attr = list(item_loc_value_moreThan50_sort_dic.keys())
        v1 = list(item_loc_value_moreThan50_sort_dic.values())
        bar = Bar("淘宝网%s卖家地址柱状图"%(search_name))
        bar.add("", attr, v1, xaxis_interval=0, xaxis_rotate=20, yaxis_rotate=11)
        bar.render("../charts/"+"淘宝网"+search_name + "卖家地址柱状图.html")

    def get_location_geo(self, db_name, search_type, search_name):
        table_name = search_name + "_" + self.types[search_type]  # 表名
        util = pymysql_util("localhost", "root", "root", 3306, db_name)
        sql = "select item_loc from " + table_name
        item_loc = util.r(sql, [])  # 查询
        item_loc_list = []
        for each in item_loc:
            if each[0].find(" ") == -1: # 如果列表里不包含该地址，则添加
                item_loc_list.append(each[0])
            else :   # 否则,去掉空格前的字符
                item_loc_list.append(each[0][each[0].find(" ") + 1:])

        item_loc_dic = {}  # 字典类型 key:地址，value：数量
        for each in item_loc_list:  # 遍历数据库中所有的地址
            item_loc_keys = numpy.array(list(item_loc_dic.keys()))
            if not item_loc_keys.__contains__(each):  # 如果列表里不包含该地址，则添加
                item_loc_dic[each] = 1
            else:  # 如果存在则数量加一
                item_loc_dic[each] += 1

        max_num = 0   # 卖家地址最多的数量
        for each in item_loc_dic.values():
            if max_num < each:
                max_num = each

        # type:list  ('深圳', 444), ('台州', 29)
        item_loc_zip_list = list(zip(tuple(item_loc_dic), tuple(item_loc_dic.values())))

        try:
            geo = Geo("全国淘宝网%s卖家分布图"%(search_name), "", title_color="#fff",
                      title_pos="center", width=1200,
                      height=600, background_color='#404a59')
            attr, value = geo.cast(item_loc_zip_list)
            geo.add("", attr, value, visual_range=[0, max_num], visual_text_color="#fff",
                    symbol_size=15, is_visualmap=True)
            geo.render("../charts/" +"淘宝网"+ search_name + "卖家地址全国分布图.html")
        except:  # 可能有些地址不在中国大陆境内
            pass

    def get_sales_geo(self, db_name, search_type, search_name):
        table_name = search_name + "_" + self.types[search_type]  # 表名
        util = pymysql_util("localhost", "root", "root", 3306, db_name)
        sql_loc = "select item_loc from "+ table_name
        sql_price = "select view_price from "+ table_name
        sql_sales = "select view_sales from "+ table_name
        item_sales = util.r(sql_sales, []) #  查询 销量
        item_price = util.r(sql_price, [])  # 查询 价格
        item_loc = util.r(sql_loc, [])  # 查询 地址
        item_loc_list = [] # 地址
        for each in item_loc:
            if each[0].find(" ") == -1: # 如果列表里不包含该地址，则添加
                item_loc_list.append(each[0])
            else :   # 否则,去掉空格前的字符
                item_loc_list.append(each[0][each[0].find(" ") + 1:])

        item_sales_list = []  # 销量
        for each in item_sales:
            item_sales_list.append(float(each[0].split("人付款")[0]))

        item_price_list = []  # 售价
        for each in item_price:
            item_price_list.append(float(each[0]))

        sales_volume = []  # 销量x售价  销售额
        for i in range(len(item_sales_list)):
            sales_volume.append(item_sales_list[i] * item_price_list[i])
        sales_volume_avg = sum(sales_volume)/len(sales_volume)    # 平均销售额

        sales_dic = {}   # key:地址 value:销售额
        for i in range(len(sales_volume)):
            if sales_dic.keys().__contains__(item_loc_list[i]):  # 如果列表里包含该地址，则数量相加
                sales_dic[item_loc_list[i]] += sales_volume[i]
            else:
                sales_dic[item_loc_list[i]] = sales_volume[i]

        geo = Geo("全国淘宝网%s销售额热图"%(search_name), "", title_color="#fff",
                  title_pos="center", width=1200,
                  height=600, background_color='#404a59')
        attr, value = geo.cast(sales_dic)
        geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, sales_volume_avg],
                visual_text_color='#fff')
        geo.render("../charts/" + "淘宝网" + search_name + "全国销售额热图.html")

class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.radio = "defalut"

    def submit(self):
        try:
            self.search_name = self.search_name.toPlainText()  # 获取单行输入框的值
            self.search_num = self.search_num.value()  # 获取数量
            self.use_db = self.use_db.toPlainText()  # 获取数据库名
            self.default_2 = self.default_2.isChecked()
            self.renqiDesc = self.renqiDesc.isChecked()
            self.saleDesc = self.saleDesc.isChecked()
            self.creditDesc = self.creditDesc.isChecked()
            self.priceAsc = self.priceAsc.isChecked()
            self.priceDesc = self.priceDesc.isChecked()
            self.totalAsc = self.totalAsc.isChecked()
            self.totalDesc = self.totalDesc.isChecked()

            self.radio_dict = {
                "defalut": self.default_2,
                "renqi-desc": self.renqiDesc,
                "sale-desc": self.saleDesc,
                "credit-desc": self.creditDesc,
                "price-asc": self.priceAsc,
                "price-desc": self.priceDesc,
                "total-asc": self.totalAsc,
                "total-desc": self.totalDesc
            }
            for key, value in self.radio_dict.items():    # 获取选中的单选框名称
                if value == True:
                    self.radio = key

            search_name = window.search_name  # 商品名
            search_num = window.search_num  # 最大查询数量
            # BUG：desc,asc是mysql关键字
            search_type = window.radio  # 查询方式
            db_name = window.use_db  # 数据库名
            # print(search_name)
            # print(search_num)
            # print(search_type)
            # print(db_name)

            spider = mikuGK_spider(search_name, search_type, self)  # 创建爬虫对象, 将商品名,搜索方式传入
            i = 0
            while True:
                i += 1
                print("正在爬取第%s" % (i) + "页")
                self.progress.setText("正在爬取第%s" % (i) + "页")
                QtWidgets.QApplication.processEvents()    # 刷新页面
                spider.get_one_page_message()  # 爬取一页数据
                spider.page += 12  # 页码加12
                if spider.page > int(search_num):  # 如果爬取数量大于预期，则break
                    break
                if spider.html_len < 10:  # 如果爬取到的页面没有数据，则break
                    break
            if not db_name == "":  # 如果没有输入数据库则不保存数据进数据库
                spider.save_in_mysql(db_name)  # 将数据存入数据库

            print("正在生成数据柱状图")
            self.progress.setText("正在生成数据柱状图")
            QtWidgets.QApplication.processEvents()  # 刷新页面
            time.sleep(2)
            chart = mikugk_location_chart()   # 创建chart对象，生成图表
            chart.get_location_bar(db_name, search_num, search_type, search_name)

            print("正在生成数据全国分布图")
            self.progress.setText("正在生成数据全国分布图")
            QtWidgets.QApplication.processEvents()  # 刷新页面
            time.sleep(2)
            chart.get_location_geo(db_name, search_type, search_name)

            print("正在生成全国销售额热图")
            self.progress.setText("正在生成全国销售额热图")
            QtWidgets.QApplication.processEvents()  # 刷新页面
            time.sleep(2)
            chart.get_sales_geo(db_name, search_type, search_name)

            print("success! Bye~")
            self.progress.setText("success! Bye~")
            QtWidgets.QApplication.processEvents()  # 刷新页面
            time.sleep(5)
            QCoreApplication.instance().quit()  # 关闭窗口
        except Exception as e:
            traceback.print_exc()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    app.exec_()








