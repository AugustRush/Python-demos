#! /usr/bin/env python
import urllib
import urllib2

from BeautifulSoup import BeautifulSoup

def getAllImagesDivs():
	page = urllib2.urlopen("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C3%D7%D3&fr=ala&ala=1&alatpl=cover&pos=0#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1")
	html = page.read()
	print html	
	soup = BeautifulSoup(html)
	liRequest = soup.findAll('li',attrs={"class":"imgshow-item"})
	for li in liRequest:
		imageSrcArray = li.findAll('img')
		
	return imageSrcArray	

print getAllImagesDivs()