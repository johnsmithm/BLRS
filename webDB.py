
import numpy as np
import glob, os, sys
from PIL import Image
import difflib
from parse import *
from getSS import *

dir = "/home/mosnoi/Desktop/Courses/IntroPR/BLRS/"
url = sys.argv[1]
short = sys.argv[2]
imgName = "img.jpg"
links  = getLinks(url,short)
links = [url] + links#ADD the url first
myset = set(links)#unique
links = list(myset)
counter = int(sys.argv[3])
end = int(sys.argv[4])
if not os.path.exists(dir+"data2/"+short):
	os.makedirs(dir+"data2/"+short)
browserSize = [[1100,700],[1000,600],[900,500],[600,400]]

s = Screenshot()
for i in links:
	for j in browserSize:
		s.capture(i, imgName,j[0],j[1])
		ii = Image.open(imgName)
		#width, height = ii.size
		#(left, upper, right, lower)
		#box = (0, 0, width, int(height/2))
		#region = ii.crop(box)
		ii.save(dir+"data2/"+short+"/"+str(counter)+".jpg")
		counter = counter + 1
	if counter > end:
		break


# python webDB.py https://www.ing.com/en.htm www.ing.com 0 10
#python webDB.py https://mijn.ing.nl/internetbankieren/SesamLoginServlet www.ing.com 82 89
# python webDB.py http://www.bnpparibas.co.uk/en/ www.bnpparibas.co.uk 0 10
# python webDB.py http://usa.bnpparibas/en/ www.bnpparibas.co.uk 0 10



				
