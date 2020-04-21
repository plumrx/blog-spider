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


def file_to_dict_list(filename):
    file = open(filename, 'r')
    content = file.read()
    string_list = content.split('\n')
    dict_list = [eval(string) for string in string_list]
    return dict_list


def main():
    dict_list = file_to_dict_list('spider-web202004191529.txt')
    db_operation(dict_list)

main()
#
# cursor = connection.cursor()
# # mycursor3.execute('CREATE TABLE testdb1(id varchar(10),url varchar(300))')
# # mycursor3.execute("ALTER TABLE testdb1 ADD COLUMN name INT AUTO_INCREMENT PRIMARY KEY")
# sql = 'INSERT INTO blog_spider(blog_name, blog_link, blog_content) VALUES(%s, %s, %s)'
# val = ('test1', 'http://1', 'bababab')
# cursor.execute(sql, val)
# connection.commit()  # 数据表内容有更


