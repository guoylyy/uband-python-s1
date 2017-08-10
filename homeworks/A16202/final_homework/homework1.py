# -*- coding: utf-8 -*-
# 任务一：词汇出现频率统计分析

# 数一数文本中各个词汇出现的次数，输出词汇的出现频率
# 1. 先用 data1/dt01.txt 的文档数据，大概200个单词，实现单词读取的类 WordReader
#    这个类的功能有几个
#    1）从一个路径里读取txt文件
#    2）把txt的文件分割成一个个单词
#    3) 对单词进行统计计数
#    4）排序
#    3）输出csv

# 2. 扩展项目，使用 data2 种的所有文件，进行第 1 步的操作，并输出成为 csv 文件
#    一般的话，我们输出成一个csv文件，方便我们能够查看到各个文件的出现次数


import codecs
import os
import csv

# 1 读取文件—————————————————————————————————————————————————

# 1.1 以“-”分割单词	
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

# 1.2 读取单个文件
def read_file(file_path):
	f = codecs.open(file_path,'r',"utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")
		words = word_split(words)
		word_list.extend(words)
	return word_list

# 1.3 读取多文件里的单词
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

# 1.4 读取文件夹中的文件路径
def get_file_from_folder(folder_path):
	file_paths = []
	for root,dirs,files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root,file)
			file_paths.append(file_path)
	return file_paths

# 2 格式化单词——————————————————————————————————————————————————
def format_word(word):
	# word = word.lower()
	fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
	for char in word:
		if char not in fmt:
			word = word.replace(char,'')
	return word.lower()

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(format_word(word))
	return word_list

# 3 统计单词数目———————————————————————————————————————————————————————
def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
# 按照单词出现的次数从多到少排列，出现次数相同的单词按照字母顺序排
	sorted_word_list = sorted(s_word_dict.items(),key=lambda kv:(-kv[1],kv[0])) 
	return sorted_word_list

# 4 list输出到csv————————————————————————————————————————————————————————
def printlist_to_csv(fileName="", dataList=[]):
	with open(fileName, "wb") as csvFile:
		csvWriter = csv.writer(csvFile)
		csvWriter.writerow(['单词','词频'])
		for data in dataList:
			csvWriter.writerow(data)
		csvFile.close

# main————————————————————————————————————————————————————
def main():
    words = read_files(get_file_from_folder('data2'))
    print '获取了未格式化的单词 %d 个' %(len(words))

    f_words = format_words(words)
    print '获取了已格式化的单词 %d 个' %(len(f_words))

    word_dic = statistics_words(f_words)
    printlist_to_csv("output/test.csv", word_dic)

if __name__ == "__main__":
    main()
