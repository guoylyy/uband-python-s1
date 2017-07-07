# -*- coding: utf-8 -*-

import codecs
class WordReader():
	def __init__(self):
		i=1
	def read_file(self, file_path):
		f=codecs.open(file_path,'r',"utf-8")
		lines=f.readlines()
		allwords=[]
		for line in lines:
			line=line.strip()
			words=line.split(" ")
			allwords=allwords+words
		return allwords

	def format_word(self, wordlist):
		fmt='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
		index=0
		for index, lst_item in enumerate(wordlist):	
			word=wordlist[index]

			for char in word:
				if char not in fmt:
					word = word.replace(char, '')
					
			wordlist[index]=word.lower()
			index=index+1
		
		#去除空值
		#wordlist.remove('')
		condition = lambda t: t != ''
		wordlist = filter(condition, wordlist)
		return wordlist

	def count_word(self,wordformat):
		wordsStat={}
		for lst_item in wordformat:
			wordsStat[lst_item] = wordformat.count(lst_item)
		return wordsStat		
   
	def sort_WordCount(self,wordcount):
		sort=sorted(wordcount.iteritems(), key = lambda e:e[1], reverse= True)
		return sort

	def print_to_csv(self,volcaulay_map, to_file_path):
		nfile = open(to_file_path,'w+')
		for index,lst_item in enumerate(volcaulay_map):
			key=lst_item[0]
			value=lst_item[1]
			
			nfile.write("%s,%s\n" % (key, str(value)))
		nfile.close()	

def main():
	data1= WordReader()
	wordlist= data1.read_file('data1/dt01.txt')
	#print wordlist
	wordformat=data1.format_word(wordlist)
	#print wordformat
	wordcount=data1.count_word(wordformat)
	#print wordcount
	wordorder=data1.sort_WordCount(wordcount)
	#print wordorder
	out= data1.print_to_csv(wordorder,'output/test.csv')
if __name__ == "__main__":
	main()
