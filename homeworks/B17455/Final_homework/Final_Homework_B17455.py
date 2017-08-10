# -*- coding: utf-8 -*-

import codecs
import os

def split_word(words):
	new_list = []
	for word in words:
		if '-' not in words:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

def read_file(file_path):
	f = codecs.open(file_path, 'r', 'utf-8')
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(' ')
		# words = split_word(words)
		# if len(words) < 20:
		word_list.extend(words)
		
	return word_list

def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths

def read_files(file_paths):
	final_work = []
	for path in file_paths:
		final_work.extend(read_file(path))
	return final_work




def format_wordlist(word_list):
	word_list2 = []
	for word0 in word_list:
		word=word0.encode('utf-8','ignore')
		# print word
		fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
		for char in word:
			if char not in fmt:
				word = word.replace(char,'')
		if (0 < len(word) <20):
			word_list2.append(word.lower())
	return word_list2



def count_words(word_list):
	dic = {}
	for item in word_list:
		if item not in dic:
			dic[item] = 1
		else:
			dic[item] += 1
	return dic

def print_to_csv(dic,to_file_path):
	output_file = open(to_file_path,'w+')
	for key in dic.keys():
		val = dic[key]
		output_file.write("%s,%s\n" % (key, val))
	output_file.close()





def main():
	path = get_file_from_folder('data2')
	# print path
	
	word_list = read_files(path)
	# # word_list = read_file('data1\dt01.txt')
	# # print word_list
	print'获取了%s个未格式化的单词 '% (len(word_list))
	f_word_list = format_wordlist(word_list) 
	# # print f_word_list
	print '获取了%d个格式化的单词 '%(len(f_word_list))
	dic = count_words(f_word_list)
	# # print dic
	print_to_csv(dic,'dnew.csv')



if __name__ == '__main__':
	main()