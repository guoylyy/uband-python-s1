#!usr/bin/python
# -*- coding: utf-8 -*-

import codecs,sys
import os,csv,re
reload(sys)
sys.setdefaultencoding('utf-8')

def readfile(PATH,filenames):
	for filename in filenames:
		file = codecs.open(PATH+"/"+filename,'r')
		lines = file.readlines()
		word_list=[]
		for line in lines:
			line=line.strip()
			line=line.upper()
			line=line.replace('’',"'")
			line=re.sub(r'[^A-Z]'," ",line)			
			words=line.split()
			word_list.extend(words)
	return word_list

def word_sum(word_list):
	word_sum={}
	for word in word_list:
		for key in word_sum:
			if word == key:
				word_sum[key]+=1
				break 
		else:
			word_sum[word]=1
	return word_sum

def main():
	PATH = "data2"
	for root,dirs,files in os.walk(PATH):
		words = readfile(PATH,files)

	word = word_sum(words)
	word = sorted(word.iteritems(),key=lambda x:x[1],reverse = True)
	csv_path=file("output/test.csv",'wb')
	csvfile=csv.writer(csv_path)
	csvfile.writerow(["word","total"])
	csvfile.writerows(word)	

if __name__ == "__main__":
    main()
