import urllib
from lxml import html
import numpy as np

short = "http://www.ing.com"
short1 = "https://www.ing.com"
url = "https://www.ing.com/en.htm"
page = html.fromstring(urllib.urlopen(url).read())

for link in page.xpath("//a"):
  #if link.get("href"):
  #	url = link.get("href")
	#print link.text
	#if link.get("href").find(short) != -1:
    		#print "Name", link.text, "URL", link.get("href")
		#print dir(link.get("href"))
	if link.get("href"):
		if link.get("href").find(short) != -1 or link.get("href").find(short1) != -1:
			print link.get("href")
print url
