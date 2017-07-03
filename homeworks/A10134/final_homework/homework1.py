#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import codecs
import os
class WordReader():
	"""docstring for WordReader"""
	def __init__(self, folder_path):
		self.folder_path=folder_path

	def get_file_form_folder(self):
		lst=[]
		for root,dirs,files in os.walk(self.folder_path):
			for file in files:
				file_path=os.path.join(root,file)
				lst.append(file_path)
		return lst

	def format_word(self,word):  # 从一个路径里读取txt文件, 把txt的文件分割成一个个单词
		fmt = 'abcdefghijklmnopqrstuvwxyz-'
		word=word.lower()
		for char in word:
			if char not in fmt:
				word = word.replace(char, '')
		return word

	def read(self):
		lst=self.get_file_form_folder()
		lst1=[]
		for file_path in lst:
			f=codecs.open(file_path,'r', "utf-8")
			lines=f.readlines()
			for line in lines:
				line=line.strip()
				words =line.split(" ")
				for word in words:
					word1=self.format_word(word)
					lst1.append(word1)
		return lst1

	def delete(self,dic,wordlist): #delete common words
		for word in wordlist:
			if dic.has_key(word):
				del dic[word]
		return dic

	def dictionary(self): #count&rank
		dic={}
		lst=self.read()
		for word in lst:
			if dic.has_key(word):
				dic[word]=dic[word]+1
			else:
				dic[word]=1
		lst=['a','the','yes','no','in','to','of','','and','is','are','that','for','it','in','on']
		dic=self.delete(dic,lst)
		lst1=sorted(dic.items(),key=lambda dic:dic[1],reverse=1)
		return lst1

	def print_to_csv(self,output_path): #输出csv
		nfile=open(output_path,'w+')

		vocabulary=self.dictionary()
		for word in vocabulary:
			nfile.write("%s,%s\n" % (word[0], word[1]))
		nfile.close()




		

def main():
 
    DATA=WordReader('data2/')
    print DATA.dictionary()
    DATA.print_to_csv('output/test.csv')
if __name__ == "__main__":
    main()
