# -*- coding: utf-8 -*-

import codecs
import os

def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
   
	lines = f.readlines()
	word_list = []

	for line in lines:
		line = line.strip()
		words = line.split(" ")
		words = word_split(words)
		word_list.extend(words)
	return word_list#都放在一个列表里面了，而不是根据句子分开好多个。

def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words



def word_split(words):
	new_lst = []
	for word in words:
		if "-" not in word:
			new_lst.append(word)
		else:
			lst = word.split("-")
			new_lst.extend(lst)
	return new_lst

#2.获取格式化之后的单词
def format_word(word):
	fmt = 'abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()


	




def format_words(words):
	word_list = []
	for word in words :
		wd = format_word(word)
		if wd:	
			word_list.append(wd)
	return word_list
	
def statistics_words(words):
	s_words_dict = {}
	for word in words:
		if s_words_dict.has_key(word):
			s_words_dict[word] = s_words_dict[word] + 1 #如果在的话
		else:
			s_words_dict[word] = 1
	return s_words_dict


def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path,'w+')
	key_list = []
	for key in volcaulay_map.keys():
		key_list.append(key)
		
		#sorted_key = sorted (key_list.items(), key = lambda item:item[1], reverse = True)#排序输出还是不会。。有几个问题：1.字典没有排序。。list和元组可以，但是用sorted 排序之后变成了由元组构成的list。。输出csv又报错。。

		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()



def main():
	
	#读取文件
		
	words =read_file("C:/Users/JIAHUI/uband-python-s1/final homework/data1/dt01.txt")
	print '获取未格式化的单词%d个 '%(len(words))

	#清洗数据
	f_words = format_words(words)
	print "获取格式化的单词%d个 "%(len(f_words)) 

	#统计和排序

	word_dict = statistics_words(f_words)
	
	#sorted_dict = sorted (word_dict.items(), key = lambda item:item[1], reverse = True)
	#print type (sorted_dict) tuple list.

	
	print_to_csv(word_dict,'output/test.csv')

if __name__ == '__main__':
	main()