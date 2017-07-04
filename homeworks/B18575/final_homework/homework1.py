#!/bin/usr/python
# -*- coding: utf-8 -*-
#@author:SKY

import os
import codecs
from wordcloud import WordCloud 
import matplotlib.pyplot as plt  

class WordReader():


	#读取文件，返回格式化后的单词字典
	def word_reader(self,file_path):
		#读取文件，分割成单词
		fp=codecs.open(file_path,'r','utf-8')
		lines=fp.readlines()
		words=[]
		for line in lines:
			line=line.strip()
			word=line.split(" ")
			words+=word
		#格式化
		fmt = 'abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ\''
		for index, word in enumerate(words):
			for char in word:
				if char not in fmt:
					word = word.replace(char, '')
			words[index]=word.lower()
		return words
	#统计单词个数
	def count_word(self,word_list):
		count={}
		for word in word_list:
			if word!='':
				if count.has_key(word):
					count[word]=count[word]+1
				else:
					count[word]=1
		return count
	#排序
	def word_sort(self,word_map):
		map={}
		list=sorted(word_map.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
		return list
		
	#输出为CSV文件
	def print_to_csv(self,to_file_path,word_list):
		fp=open(to_file_path,'w+')
		for item in word_list:
			fp.write("%s,%s\n" % (item[0],item[1]))
		fp.close()

def main():
	wr=WordReader()
	wlist=wr.word_reader('data1/dt01.txt')
	word_map=wr.count_word(wlist)
	word_list=wr.word_sort(word_map)
	# wr.print_to_csv('output/test1.csv',word_list)

	wcount=[]
	for root,dirs,files in os.walk('data2'):
		for file in files:
			file_path=os.path.join(root,file)
			wlist=wr.word_reader(file_path)
			wcount+=wlist
	word_map=wr.count_word(wcount)
	word_list=wr.word_sort(word_map)
	wr.print_to_csv('output/test2.csv',word_list)




if __name__ == "__main__":
    main()
