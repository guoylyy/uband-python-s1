#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu

import codecs
import os

#根据‘-’划分单词
def word_split(words):
	nlist = []
	for word in words :
		if '-' not in word:
			nlist.append(word)
		else:
			lst = word.split('-')
			nlist.extend(lst)
	return nlist

#读取单个文件#
def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	wordss = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")#根据‘’划分单词
		words = word_split(words)#根据‘-’再次划分单词
		wordss.extend(words)
		# print wordss
	return wordss
	txt.close()

# #读取多个文件
# def read_files(file_paths):
# 	wordss = []
# 	for file_path in file_paths:
# 		words = read_file(file_path)
# 		wordss.extend(words)
# 	return wordss
 
 #将单词中的非字母符号去掉，并将大写字母转换为小写
def format_word(word):
	fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()

#将所有单词中的非字母符号去掉，并将大写字母转换为小写，去掉空字符组成的单词
def format_words(words):
	wordss = []
	for word in words:
		wd = format_word(word)
		if wd != '':
			wordss.append(wd)
	return wordss

#用字典计算每个单词出现的次数
def count(words):
	lst = {}
	for index, word in enumerate(words):
		if lst.has_key(word):
			lst[word] = lst[word] + 1
		else:
			lst[word] = 1
	# print lst
	return lst 

#将字典输出为.csv格式
def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path,'w+')
	for key in volcaulay_map.keys():
		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()

# #获取文件夹中的所有文件路径
# def get_file_from_folder(folder_path):
# 	file_paths = []
# 	for root, dirs, files in os.walk(folder_path):
# 		for file in files:
# 			file_path = os.path.join(root, file)
# 			file_paths.append(file_path)
# 			# print file_path
# 	return file_paths


def main():
#1.读取文本
	words = read_file('data1/dt01.txt')
	# print words
	# file_paths = get_file_from_folder('data2')
	# words = read_files(get_file_from_folder('data2'))
	print '未格式化单词 %d 个' % (len(words))
#2.清洗文本
	words = format_words(words)
	print '格式化的单词 %d 个' % (len(words))
#3.统计单词
	lst = count(words)
	# print lst
#4.输出为.cvs文件
	print_to_csv(lst,'output/test.csv')


if __name__ == '__main__':
	main()