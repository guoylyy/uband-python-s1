# -*- coding: utf-8 -*-

import codecs
import os


def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list=[]
	for line in lines:
		line = line.strip()
		words = line.split(' ')
		word_list.extend(words)	
	return word_list

def format_word(word):
	fmt = 'abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word=word.replace(char,'')
	return word.lower()

def format_words(words):
	word_list = []

	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
	return word_list


def main():
	words=read_file('data1/dt01.txt')
	print '获取了%d个未格式化的单词'%(len(words))
	print words
	
	f_words=format_words(words)
	print '获取已经格式化的单词%d个'%(len(f_words))
	print f_words
	
if __name__ == "__main__":
    main()
