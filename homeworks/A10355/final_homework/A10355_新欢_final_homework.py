# -*- coding: utf-8 -*-

import codecs
import os

#分割有-的单词
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

# 读取一个文件
def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	words_all = []
	# print len(words_all)
	for line in lines:
		line = line.strip()		#去掉每行首尾空格
		words = line.split(" ")		#分割单词
		words = word_split(words)
		words_all.extend(words)
	return words_all

# 读取多个文件
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

# 获取格式化之后的单词
def format_word(word):
	fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()		#变小写

def format_all(words):
	words_list = []
	for words_item in words:
		# print words_item
		word = format_word(words_item)
		if word:
			words_list.append(word)
	return words_list 

# 统计单词个数
def count(words):
	dictionary = {}
	for index in range(len(words)):
		if not dictionary.has_key(words[index]):	#添加新词
			dictionary[words[index]] = 1
		else:
			dictionary[words[index]] = dictionary[words[index]]+1
	return dictionary

# 读取文件夹里的所有文件
def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			# print file_path
			file_paths.append(file_path)
	return file_paths

# 输出csv文件
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def main():
	#1. 读取文本
	# words = read_file('data1/dt01.txt')
	words = read_files(get_file_from_folder('data2'))
	# print words
	print 'obtained %s words' %(len(words))

	#2. 清洗文本
	f_words = format_all(words)
	# print f_words
	print 'obtained %s format words' %(len(f_words))

	#3. 统计计数
	dictionary = count(f_words)
	# print dictionary
	print 'obtained %s unrepeated words' %(len(dictionary))

	#4. 排序（未完场）
	# order_list=sorted(dictionary.items(),key=lambda item:item[1],reverse=True)
	# print order_list
	# for order_list_item in order_list:
	# 	print order_list_item

	#5. 输出csv
	print_to_csv(dictionary,'output/test.csv')
	print 'output file success'
	# nfile = open(to_file_path,'w+')
	# for order_list_item in order_list:
	# 	# val = volcaulay_map[key]
	# 	nfile.write("%s\n" % (str(order_list_item))
	# nfile.close()


if __name__ == "__main__":
	main()
