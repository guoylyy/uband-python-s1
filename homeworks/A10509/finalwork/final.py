#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vnicorn

import codecs
import os

#读取文件夹里的所有文件
def get_file_from_folder(folder_path):
	paths_list = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			paths_list.append(file_path)
	return paths_list            

def read_files(paths_list):
	filewords = [] 
	for paths in paths_list:
		filewords.extend(read_file(paths))
	return filewords

def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    words_list = []
    for line in lines:
    	line = line.strip()
        words = line.split(" ")# 空格
        words2 = wordsplit(words)
        words_list.extend(words2)
    return words_list


def wordsplit(words):
	word_list2 = []
	for w in words:
		if '-' in w:
			lst = w.split('-')
			word_list2.extend(lst)
		else:
			word_list2.append(w)
	return word_list2

#清洗
def format_word(word):
	word = word.lower()
	fmt = 'abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list
#统计
def statics(word_list):
	dict = {}
	for word in word_list:
		if dict.has_key(word):
			dict[word] = dict[word] + 1
		else:
			dict[word] = 1
	return dict
	
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def main():
	filewords = read_files(get_file_from_folder('data'))
	format_words(filewords)
	word_list = format_words(filewords)
	statics(word_list)
	dict = statics(word_list)
	print_to_csv(dict, 'data/output.csv')

if __name__ == '__main__':
  main()