
import numpy as np
import glob, os
from PIL import Image
import difflib
dir = "/home/mosnoi/Desktop/Courses/IntroPR/BLRS/"
os.chdir(dir+"BankPhishing")
files = []
for file in glob.glob("*.jpg"):
	ok = "no"
	ii = Image.open(dir+"BankPhishing/"+file)
	width, height = ii.size
	#(left, upper, right, lower)
	box = (0, 0, width, int(height/2))
	region = ii.crop(box)
	for ex in files:
	    #if ex[:-4].find(file[:-4])!=-1 or file[:-4].find(ex[:-4])!=-1:
	    #	ok = ex
		nr = 0
		for i,s in enumerate(difflib.ndiff(file,ex)):
			if s[0] != ' ':
				nr = nr + 1
		if (nr < 5 and (len(ex) > 8 or len(file) > 8)) or (nr < 2):
			ok = ex
				
	if ok is "no":
		files.append(file)
		if not os.path.exists(dir+"data/"+file[:-4]):
			os.makedirs(dir+"data/"+file[:-4])
		region.save(dir+"data/"+file[:-4]+"/"+file)
	else:
		
		region.save(dir+"data/"+ok[:-4]+"/"+file)
				
