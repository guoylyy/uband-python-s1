#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小八
import codecs
import os


#1.获取文本
def word_split(words):#分割单词
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")#打开文件
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")#用空格分割
		words = word_split(words)#用-分割
		word_list.extend(words)
	return word_list

#2.获取格式化的单词
def format_word(word):#格式化一个单词
	fmt = 'abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()

def format_words(words):
	word_list = []
	for  word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#3.统计单词数目
def statistics_words(words):
 	s_word_dict = {}
 	for word in words:
 		if s_word_dict.has_key(word):
 			s_word_dict[word] = s_word_dict[word] + 1
 		else:
 			s_word_dict[word] = 1
 	return s_word_dict	

#4.输出成CSV
def print_to_csv(vocabulary_map, to_file_path):
	nfile = open(to_file_path, 'w+')
	for key in vocabulary_map.keys():
		val = vocabulary_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()

def main():
	#1.读取文本
	words = read_file('data1/dt01.txt')
	print '获取了未格式化的单词 %d 个' % (len(words))
	#2.清洗文本
	f_words = format_words(words)
	print f_words
	print '获取了已经格式化的单词 %d 个' % (len(f_words))

	#3.统计单词和排序
	word_dict = statistics_words(f_words)

	#4.输出文件
	print_to_csv(word_dict, 'data1/test.csv')


if __name__ == '__main__':
  main()