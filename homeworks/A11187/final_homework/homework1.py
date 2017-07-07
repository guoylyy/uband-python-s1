# -*- coding: utf-8 -*-

import codecs
import os

#1. 读取文件
def word_split(words):
	word_list2 = []
	for word in words:
		if '-' not in word:
			word_list2.append(word)
		else:
			lst = word.split('-')
			word_list2.extend(lst)
	return word_list2

def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")
		words = word_split(words)
		word_list.extend(words)
	return word_list

def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths

def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

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
		standard = format_word(word)
		if standard:
			word_list.append(standard)
	return word_list

#3.统计单词数
def count_words(words):
	c_word_dict = {}
	for word in words:
		if c_word_dict.has_key(word):
			c_word_dict[word] = c_word_dict[word] + 1
		else:
			c_word_dict[word] = 1
	return c_word_dict
	sorted(c_word_dict.items(), key = lambda e:e[1], reverse = True)
	

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path,'w+')
	for key in volcaulay_map.keys():
		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()

def main():
	#words = read_file('data1/dt01.txt')
	words = read_files(get_file_from_folder('data2'))
	print 'get the number of unformatted words: %d ' % (len(words))

	f_words = format_words(words)
	print 'get the number of formatted words: %d ' % (len(f_words))

	word_dict = count_words(f_words)

	print_to_csv(word_dict, 'output/test.csv')

if __name__ == '__main__':
	main()
