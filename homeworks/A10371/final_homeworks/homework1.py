#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
import codecs
import os

 #1.读取文件
 #1)去掉-分隔符  
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list
#2）去掉空格
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip() #把空格去掉
        words = line.split(' ') #按空格分割
    	words = word_split(words) 
        word_list.extend(words)
    return word_list

#3）读多文件，获取文件名
def get_file_from_folder(folder_path):
 	file_paths = []
 	for root, dirs, files in os.walk(folder_path):
 		for file in files:
 			file_path = os.path.join(root, file)
 			file_paths.append(file_path)
 	return file_paths
#4）读多个文件
def read_files(file_paths):
 	final_words = []
 	for path in file_paths:
 		final_words.extend(read_file(path))
 	return final_words


#2.获取格式化之后的单词
def format_word(word):
    fmt='abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word=word.replace(char, '')
    return word.lower()

def format_words(words):
 	word_list = []
 	for word in words:
 	    wd = format_word(word)
 	    if wd: 
 			word_list.append(wd)
 	return word_list

#3.1统计单词频率
def statictcs_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict

#3.2排序
def sorted_words():
	sorted_words = sorted(word_dict.items(),key=lambda item:item[1],reverse=True)

#4.输出成csv文件
def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path,'wt')
	for key in volcaulay_map.keys():
		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()

def main():
	
	#1.读取文本
	#words = read_file('data1/dt01.txt')
	words = read_files(get_file_from_folder('data2'))
	print '获取了未格式化的单词 %d 个 ' % (len(words))
    #2.清洗文本
	f_words=format_words(words)
	
	print '获取了已格式化的单词 %d 个 '  % (len(f_words)) 
    #3.统计单词和排序
	word_dict = statictcs_words(f_words)
	#排序
	print sorted(word_dict.items(),key=lambda item:item[1],reverse=True)
  
    #4.输出文件
	print_to_csv(word_dict, 'output/testdata5.csv')

if __name__ == "__main__":
    main()
