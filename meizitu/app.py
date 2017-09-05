#coding: utf-8
import requests
from lxml import html
import os

import time

def getLinks():
    baseUrl = 'http://www.cutestpaw.com/tag/koalas/'
    selector=html.fromstring(requests.get(baseUrl).content)


    urls=[]
    for i in selector.xpath('//img/@src'):
        urls.append(i)
    return urls

def downloader(mylinks,dirName):
    os.mkdir(dirName)
    count=1
    for i in mylinks:
        # 文件写入的名称：当前路径／文件夹／文件名
        filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, count)
        print u'开始下载图片:%s 第%s张' % (dirName, count)
        with open(filename, "wb") as jpg:
            jpg.write(requests.get(i).content)
            time.sleep(0.5)
        count += 1
        if count > 20:
            break


if __name__=="__main__":
    urls=getLinks()
    # for url in urls:
    #     print url
    downloader(urls,"mykoalas")
