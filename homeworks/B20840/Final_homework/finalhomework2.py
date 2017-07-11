#!/usr/bin/python
#_*_ coding: utf-8 _*_
#@author: B20840

import codecs
import os

#1.读取文件
def word_split(words):
	new_list =[]
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list


def read_file(file_path):
	f = codecs.open(file_path,'r',"utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ") #用空格分割
		words = word_split(words) #用-分割
		word_list.extend(words)	
	return word_list

#读取一组文件路径
def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root,file)
			file_paths.append(file_path)
	return file_paths



#读取多文件中的单词
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words
	
#2.获取格式化之后的单词
def format_word(word):
	fmt ='abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char,'')
			
	return word.lower()

#读取多文件里面的单词
def format_words(words):
	word_list=[]
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(format_word(word))
	return word_list

#3.统计单词数目
#{'aa':4,'bb':1}
def statistic_words(words):
	s_word_dict={}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word]+1
		else:
			s_word_dict[word]=1
	return s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path, 'w+')
	for key in volcaulay_map.keys():
		val=volcaulay_map[key]
		nfile.write("%s,%s\n" %(key,str(val)))
	nfile.close()


def main():
	#1. Read document
	#words = read_file('data1/dt01.txt')
	#paths = get_file_from_folder('data2')
	#read_file('/Users/yuanjun/Desktop/WEEK FOUR/大作业/final-homework/data2/2016.01.02.TXT')
	words = read_files(get_file_from_folder('data2'))
	print '获取了已经格式化的单词 %d 个' %(len(words))
	#print '获取了未格式化的单词%d个' %(len(words))
	
	#2. 清洗文本
	f_words = format_words(words)
	#print f_words
	print '获取了已经格式化的单词 %d 个' %(len(f_words))
	
	#3. 统计单词和排序
	word_dict = statistic_words(f_words)

	#4. 输出文件
	print_to_csv(word_dict, 'output/finalhomework2.csv')


if __name__ == '__main__':
	main()