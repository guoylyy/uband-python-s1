#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: fanyujie

import codecs
import os


def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")
		word_list.extend(words)
	return word_list


def format_word(word):
	fmt = 'abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()

def format_words(words):
	word_list = []
	for word in words:
		word_list.append(format_word(word))
	return word_list

def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict


# def get_file_from_folder(folder_path):
# 	for root, dirs, files in os.walk(folder_path):
# 		for file in files:
# 			file_path = os.path.join(root, file)
# 			print file_path

def print_to_csv(vocabulary_map, to_file_path):
	nfile = open(to_file_path, 'w+')
	for key in vocabulary_map.keys():
		val = vocabulary_map[key]
		nfile.write("%s, %s\n" % (key, str(val)))
	nfile.close()



def main():
	words = read_file('data1/dt01.txt')
	print "unformatized %d" % (len(words))
	f_words = format_words(words)
	print f_words
	print 'formated %d' % (len(f_words))
	word_dict = statistics_words(f_words)
	print_to_csv(word_dict, 'output/test.csv')

if __name__ == '__main__':
	main()
  
