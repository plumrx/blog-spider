import mysql.connector

#
# #创建数据库链接
# mydb1 = mysql.connector.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",       # 数据库用户名
#     passwd=""          # 数据库密码
# )
#
# print(mydb1)
#
# #新建数据库
# #创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 runoob_db 的数据库
# mydb2 = mysql.connector.connect(
#     host="localhost",
#     user='root',
#     passwd=''
# )
#
# # mycursor= mydb2.cursor()
# # mycursor.execute('CREATE DATABASE mysqltest1')
#
# #输出所有数据库列表
# mycursor1 = mydb1.cursor()
#
# mycursor1.execute("SHOW DATABASES")
#
# for x in mycursor1:
#     print(x)


# 直接链接数据库
# 建表
# 插入主键 alert add column
# 插入数据 insert into
mydb3 = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='BlogSpider'
)

mycursor3 = mydb3.cursor()
# mycursor3.execute('CREATE TABLE testdb1(id varchar(10),url varchar(300))')
# mycursor3.execute("ALTER TABLE testdb1 ADD COLUMN name INT AUTO_INCREMENT PRIMARY KEY")
sql = 'INSERT INTO blog_spider(blog_name, blog_link, blog_content) VALUES(%s, %s, %s)'
val = ('test1','http://1','bababab')
mycursor3.execute(sql, val)
mydb3.commit()  # 数据表内容有更新











