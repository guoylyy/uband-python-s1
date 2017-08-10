# -*- coding: utf-8 -*-

import codecs
import os

def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst= word.split('-')
			new_list.extend(lst)
	return new_list


def read_file(file_path):
	f = codecs.open(file_path,'r',"utf-8") 
	lines = f.readlines()
	word_list= []

	for line in lines:
		line = line.strip()
		words = line.split(' ')
		words = word_split(words)
		word_list.extend(words)
		
	return word_list

def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs,files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths

def read_files(file_paths):
	final_words= []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words


def format_word(word):
	fmt='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'

	for char in word:
		if char not in fmt:
			word = word.replace(char,'')

	return word.lower()

def format_words(words):
	word_list=[]

	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word]+1
		else:
			s_word_dict[word] = 1

	return s_word_dict

	

def print_to_csv(vocabulary_map,to_file_path):
	nfile=open(to_file_path,'w+')

	for key in vocabulary_map.keys():
		values=vocabulary_map[key]
		nfile.write("%s,%d\n"%(key,values))
		sorted(vocabulary_map.items(),key=lambda x:x[1],reverse=True)

	return nfile.write




	nfile.close()



def main():
	words=read_files(get_file_from_folder('data2'))
	print '获取未格式化单词%d个' %(len(words))
	f_words=format_words(words)
	print '获取已格式化单词%d个' %(len(f_words))
	word_dict=statistics_words(f_words)
	print_to_csv(word_dict,'output/sudo python test.csv')


if __name__ == '__main__':
	main()



