#! /usr/bin/env python
import urllib2

def getPageHtml(urlString):
	request = urllib2.Request(urlString)
	page = urllib2.urlopen(request)
	html = page.read()
	return html

print getPageHtml("http://mm.taobao.com/json/request_top_list.htm")