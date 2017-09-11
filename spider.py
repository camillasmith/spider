#!usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    html=html.decode('utf-8')
    print(html)

def getImg(html):
    #html=html.decode('utf-8')
    reg=r"URL.\.jpg"
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    print(imglist)
html=getHtml("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87")
img=getImg(html)
print(img)

