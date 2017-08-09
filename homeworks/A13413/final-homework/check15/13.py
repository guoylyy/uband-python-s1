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

def main():
	words=read_file('data1/dt01.txt')

	print words
	print'一共有%d个单词'%(len(words))
	

if __name__ == '__main__':
	main()
