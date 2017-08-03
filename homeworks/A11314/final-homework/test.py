import os
PATH = "data"
for root,dirs,files in os.walk(PATH):
	print  "%s/%s" %(root,files)

	# words = readfile(files)