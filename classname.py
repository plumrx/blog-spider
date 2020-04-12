# web-spider.py
# <span itemprop="name">Flutter 学习笔记</span> 文章名称

import time
import requests
from bs4 import BeautifulSoup


# 示例
def testWeb(url, element):
    # url = 'https://blog.mutoe.com/archives/'  # 目标地址
    # 实例化固定套路??
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    for course in soup.find_all(element):
        # 打印该标签属性
        print(course.text)


# testWeb('http://www.itest.info/courses','h4')


'''
1 文章名
2 文章链接
3 文章正文
'''


def blog(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # 用不用self的区别??
    fileNameList = []
    for span in soup.find_all('span', itemprop='name'):
        print(span.text)
        fileNameList.append(span.text)

    file = open('spiderResuult-3.txt', 'a')
    file.write('\n'.join(fileNameList))



def getResponse(url):
    res = requests.get(url)
    res.encoding = 'utf-8'  # 转码
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def createFile(filename, list):
    file = open(filename, 'w')
    file.write('\n'.join(list))


# https://blog.mutoe.com/
def blogInformation(url):
    t = time.time()
    localTime = time.strftime('%Y%m%d%H%M', time.gmtime(t))
    resText = getResponse(url)
    # 文章信息列表
    blog_information_list = []
    for titlElement in resText.find_all('a', class_='post-title-link'):
        blogDict = dict()  # 定义字典 {'name':'firstBlog','link':'http://...','context':'首先。。。。其次。。'}
        blogDict['name'] = titlElement.text
        blogDict['link'] = url + titlElement.get('href')
        # 每篇文章
        resContent = getResponse(blogDict['link'])
        blogDict['content'] = resContent.find('div', class_='post-body').prettify()
        blog_information_list.append(blogDict)

    print(blog_information_list)
    string_list = map(lambda info: str(info), blog_information_list)


    createFile('spider' + localTime + '.txt', string_list)

blogInformation('https://blog.mutoe.com')

