# -*- coding: utf-8 -*-


import codecs
import os

#1. 读取文件
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

def read_file(file_path):
    file = codecs.open(file_path, 'r', "utf-8")
    lines = file.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ") #define "words", a word is sth splited by space
        words = word_split(words)
        word_list.extend(words) #extend word list 
    return word_list

def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths


def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:  #define "word", a word is sth constitutes with alpha-beta 
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

#apply to a set of words
def format_words(words): 
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd: #non zero
			word_list.append(wd)
	return word_list

#3. statistics
def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():	
 
	words = read_files(get_file_from_folder('data2'))
	print 'Creates %d raw words' % (len(words))


	f_words = format_words(words)
	print 'Creates %d formate words' % (len(f_words))

	
	s_words = statistics_words(f_words)


	print_to_csv(s_words, 'output/test.csv')

if __name__ == "__main__":
    main()
