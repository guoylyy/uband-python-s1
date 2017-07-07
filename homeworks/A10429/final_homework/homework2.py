# -*- coding: utf-8 -*-

import codecs
import os
from collections import Counter
#定义一个类
class WordReader():
	def __init__(self):
		pass
	#读取文件夹里所有文件
	def get_file_from_folder(self,folder_path):
		allfile_path=[]
		for root,dirs,files in os.walk(folder_path):
			for file in files:
				file_path = os.path.join(root,file)
				allfile_path.append(file_path)
		return allfile_path

	#读取单个文件
	def read_file(self, file_path):
		allwords = []
		f = codecs.open(file_path,'r',"utf-8")
		lines = f.readlines() #读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素
		for line in lines:
			line = line.strip() #去除前后空格
			words = line.split(" ") #读取该行的字符，以空格分割，保存在一个list中，每个word是个元素
			allwords = allwords + words #该文件的所有行里的单词组成的list
		return allwords

	#获取格式化的单词
	def format_word(self, word):
		fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
		for char in word:
			if char not in fmt:
				word = word.replace(char,'')#其他字符替换成空格
		return word.lower() #一律变成小写

	#数单词个数
	def count_word(self,wordformat):
		return Counter(wordformat)
	# def count_word(self,wordformat):
	# 	wordsStat={}
	# 	for lst_item in wordformat:
	# 		wordsStat[lst_item] = wordformat.count(lst_item)
	# 	return wordsStat		

	#排序
	def sort_WordCount(self,wordcount):
		sort=sorted(wordcount.iteritems(), key = lambda e:e[1], reverse= True)
		return sort

	#输出成csv
	def print_to_csv(self, vocabulary_map, to_file_path):
		nfile = open(to_file_path,'w+')
		for index,lst_item in enumerate(vocabulary_map):
			key=lst_item[0]
			value=lst_item[1]
			
			nfile.write("%s,%s\n" % (key, str(value)))
		nfile.close()

def main():
	file1	= WordReader()
	allword_list = []

	for lst_item in file1.get_file_from_folder('data2'): #遍历所有文件
		words = file1.read_file(lst_item) #该文件中的所有单词构成的列表
		for index, lst_item in enumerate(words):	
			words[index] = file1.format_word(lst_item)#将所有单词格式化
		allword_list = allword_list + words #得到了所有文件里的所有单词
	
	condition = lambda t: t != ''
	allword_list = filter(condition, allword_list)#去除空格
	
	wordcounts = file1.count_word(allword_list)	

	sortresult = file1.sort_WordCount(wordcounts)

	file1.print_to_csv(sortresult,'output/test2.csv' )


		


if __name__ == '__main__':
	main()