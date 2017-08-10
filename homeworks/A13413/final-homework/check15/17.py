# -*- coding: utf-8 -*-

import codecs
import os

def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(' ')
		word_list.extend(words)
	return word_list

def format_word(word):
	fmt = 'aasdfghjklpeioewuifjid-'
	for char in word:
		if char not in fmt:
			word = word.replace(char,' ')
	return word.lower() 
def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd: 
			word_list.append(wd)
	return word_list
def statictcs_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word]=s_word_dict[word]+1
		else:
			s_word_dict[word]=1
	return s_word_dict
def print_to_csv(vocabulary_map, to_file_path):
	nfile = open(to_file_path, 'w+')
	for key in vocabulary_map.keys():
		values = vocabulary_map[key]
		nfile.write("%s, %s\n"%(key,values))
	nfile.close()

def main():
	words=read_file('data1/dt01.txt')
	f_words=format_words(words)
	word_dict=statictcs_words(f_words)

	print_to_csv(word_dict,'output/test.csv')
	
if __name__ == '__main__':
	main()