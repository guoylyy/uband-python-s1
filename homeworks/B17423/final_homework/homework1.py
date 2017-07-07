#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

import codecs  
import os
import re  #正则表达式

class WordReader():
	"""docstring for WordReader"""
	def __init__(self):
		self.wordlist = {}  #定义空字典

	#1. 从一个路径里读取txt文件
	#2. 把txt的文件分割成一个个单词
	def getFile(self, path):
		# 用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode 
		f = codecs.open(path, 'r', 'utf-8')
		lines = f.readlines()   #分行读取
		for line in lines:
			line = line.strip()  #移除字符串头尾指定的字符(默认为空格)
			words = line.split(" ") #空格分隔字符串
			#print (words)
			for word in words:
				w = self.formatWord(word)  #格式化
				if w:           #删除空格
					if w in self.wordlist:
						self.wordlist[w] = self.wordlist[w] +1
					else:
						self.wordlist[w] = 1    #单词加入wordlist

	#读取文件夹里的所有文件
	def get_file_from_folder(self, folder_path):
		for root, dirs, files in os.walk(folder_path):
			for file in files:
				file_path = os.path.join(root, file)
				self.getFile(file_path)

		#单词格式化
	def formatWord(self, word):
		# if re.search('[a-zA-Z-]',word):
		# 	return word.lower
		# else:
		# 	return ''
		fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
		for char in word:
			if char not in fmt:
				word = word.replace(char, '')  #删除不是字母或-的字符
		return word.lower()   #单词变小写


	#3. 对单词进行统计计数
	def getCount(self):
		return len(self.wordlist)

	#4. 按单词出现次数排序
	def sortWords(self):
		self.wordlist = sorted(self.wordlist.items(), key=lambda item:item[1], reverse=True)  #排序后成为元组组成的列表

	#5. 输出到csv
	def print_to_csv(self, to_path):
		to_file = open(to_path, 'w+')
		for tup in self.wordlist:
			key = tup[0]       #打印元组组成的list
			value = tup[1]
		# for key in self.wordlist:
		# 	value = self.wordlist[key]
			to_file.write("%s,%s\n" % (key, str(value)))
		to_file.close()



def main():
    reader = WordReader()
    #reader.getFile('data1/dt01.txt')   #单个文件

    reader.get_file_from_folder('data2') #多个文件
    print ("单词读取完毕，格式化后共%d个单词\n" % reader.getCount())
    reader.sortWords()
    reader.print_to_csv('output/test.csv')


if __name__ == "__main__":
    main()
