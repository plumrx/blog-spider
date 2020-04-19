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


#直接链接数据库，建表
mydb3 = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='BlogSpider'
)

mycursor3 = mydb3.cursor()
mycursor3.execute('CREATE TABLE testdb1(id varchar(10),url varchar(300));')












