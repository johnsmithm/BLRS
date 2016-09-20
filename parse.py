import urllib
from lxml import html
import numpy as np


def getLinks(url, short):
	links = list()
	page = html.fromstring(urllib.urlopen(url).read())

	for link in page.xpath("//a"):
		if link.get("href"):
			if link.get("href").find(short) != -1:
				links.append(link.get("href"))
	return links
