# -*- coding: utf-8 -*-

import codecs
import os

#1. 读取文件
#['aa','bb-cc']=>['aa','bb','cc']
# def word_split(words):
# 	new_list = []
# 	for word in words:
# 		if '-' not in word:
# 			new_list.append(word)
# 	else:
# 		lst = word_split('-')
# 		new_list.extend(lst)
# 	return new_list

def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")#用空格分割
		# words = word_split(words)
		word_list.extend(words)
	return word_list

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()    

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:	
			word_list.append(wd)
	return word_list

#3.统计单词数目
def statistic_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path,'w+')
	for key in volcaulay_map.keys():
		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()


def main():
	#1.读取文本
	words = read_file('data2/2016.01.02.txt')
	#print words
	print '获取了未格式化的单词 %d 个' % (len(words))
	
	#2.清洗文本
	f_words = format_words(words)
	#print f_words
	print '获取了已格式化的单词 %d 个' % (len(f_words))
	
	#3.统计单词和排序
	word_dict = statistic_words(f_words)

	#4.输出文件
	print_to_csv(word_dict, 'output/test.csv')

if __name__ == '__main__':
	main()