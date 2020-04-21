# classname.py

import time
import requests
from bs4 import BeautifulSoup
import mysql.connector



# dict->sql
def dict_to_sql(blog_dict, table_name='posts'):
    # 将dict转化为可遍历的元组数组
    dict_entities = [(key, value) for key, value in blog_dict.items()]
    # 拼接列名
    column_names = ','.join(dict_entity[0] for dict_entity in dict_entities)
    column_values = ','.join(repr(dict_entity[1]) for dict_entity in dict_entities)
    sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, column_names, column_values)
    return sql

# 直接链接数据库
# 建表
# 插入主键 alert add column
# 插入数据 insert into
def db_operation(dict_list):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='BlogSpider'
    )

    cursor = connection.cursor()

    for blog_dict in dict_list:
        sql = dict_to_sql(blog_dict)
        cursor.execute(sql)
    connection.commit()

# 创建文件
def createFile(filename, filelist):
    file = open(filename, 'w')
    file.write('\n'.join(filelist))


# 转换时间
def exchangeTime(mode):
    t = time.time()
    exchangedTime = time.strftime(mode, time.gmtime(t))
    return exchangedTime


# 获取目标地址内容
def getRquests(url):
    response = requests.get(url)
    response.encoding = 'utf-8'  # 转码
    res = response.text
    soup = BeautifulSoup(res, 'html.parser')
    return soup


# <a href="/2020/flutter-study-notes/" class="post-title-link" itemprop="url">Flutter 学习笔记</a>
# <div class="post-body" itemprop="articleBody" >

# 获取文章名、文章地址、文章内容
def getBlogInfo(url, filename):
    blogInfoList = []

    # 获取博客信息
    response = getRquests(url)
    for elements in response.find_all('a', class_='post-title-link'):
        blogInfoDict = dict()
        blogInfoDict['name'] = elements.text
        blogInfoDict['link'] = url + elements.get('href')

        # 获取每篇博文
        blog = getRquests(url + elements.get('href'))
        blogInfoDict['blog'] = blog.find('div', class_='post-body').prettify()

        # 把字典信息加入到数组中
        blogInfoList.append(blogInfoDict)
        blogInfoStrList = map(str, blogInfoList)
    # 创建文件名带时间的TXT文件
    createFile(filename, blogInfoStrList)
    db_operation(blogInfoList)


getBlogInfo('https://blog.mutoe.com', 'spider-web' + exchangeTime('%Y%m%d%H%M') + '.txt')



# # 数据库
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     database='BlogSpider'
# )
#
# mycursor = mydb.cursor()
# # mycursor3.execute('CREATE TABLE testdb1(id varchar(10),url varchar(300))')
# # mycursor3.execute("ALTER TABLE testdb1 ADD COLUMN name INT AUTO_INCREMENT PRIMARY KEY")
# sql = 'INSERT INTO blog_spider(blog_name, blog_link, blog_content) VALUES(%s, %s, %s)'
# val = ('test1','http://1','bababab')
# mycursor.execute(sql, val)
# mydb.commit()  # 数据表内容有更新
