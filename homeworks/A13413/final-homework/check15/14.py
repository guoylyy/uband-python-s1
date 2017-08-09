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

def main():
	words=read_file('data1/dt01.txt')
	print format_word('A2as')
if __name__ == '__main__':
	main()