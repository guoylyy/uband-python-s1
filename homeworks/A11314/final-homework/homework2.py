#!usr/bin/python
# -*- coding: utf-8 -*-

import codecs,sys
import os,csv,re
reload(sys)
sys.setdefaultencoding('utf-8')

def readfile(PATH,filenames):
	word_list=[]
	for filename in filenames:
		file = codecs.open(PATH+"/"+filename,'r')
		lines = file.readlines()

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
		if word_sum.has_key(word):
			word_sum[word]+=1
		else:
			word_sum[word]=1
	return word_sum


def main():
	PATH = "data2"
	for root,dirs,files in os.walk(PATH):
		words = readfile(PATH,files)
	print "获取到的单词共%d个" %len(words)
	word = word_sum(words)
	word = sorted(word.iteritems(),key=lambda x:x[1],reverse = True)
	csv_path=file("output/test2.csv",'wb')
	csvfile=csv.writer(csv_path)
	csvfile.writerow(["word","total"])
	csvfile.writerows(word)	

if __name__ == "__main__":
    main()
