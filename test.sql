select * from blog_spider;

insert into blog_spider(id, blog_name, blog_link, blog_content, create_date)
values
(001, 'test1', 'https://mutoe.blog.com', 'insert data1 ', CURRENT_TIME());

insert into blog_spider(id, blog_name, blog_link, blog_content, create_date)
values
(002, 'test2', 'https://mutoe.blog.com', 'insert data1 ', NOW());

