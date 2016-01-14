#! /usr/bin/env python
import urllib
import urllib2

from Scrapy import Scrapy

def getAllImagesDivs():
	request = urllib2.Request(url='https://dribbble.com/shots?list=animated',headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} )
	page = urllib2.urlopen(request)
	html = page.read()
	print html	
	soup = BeautifulSoup(html)
	liRequest = soup.findAll('p',attrs={"class":"follow"})
	print 'librequest is ',librequest
	for li in liRequest:
		imageSrcArray = li.findAll('img')