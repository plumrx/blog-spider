# classname.py

import time
import requests
from bs4 import BeautifulSoup


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


getBlogInfo('https://blog.mutoe.com', 'spider-web' + exchangeTime('%Y%m%d%H%M') + '.txt')
