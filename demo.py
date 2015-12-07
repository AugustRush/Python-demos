#! /usr/bin/env python
import urllib
import urllib2

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getHtml2(url):
	request = urllib2.Request(url)
	page = urllib2.urlopen(request)
	html = page.read()
	return html

html = getHtml("http://tieba.baidu.com/p/2738151262")
html2 = getHtml2("http://www.baidu.com/")

print html
print html2
