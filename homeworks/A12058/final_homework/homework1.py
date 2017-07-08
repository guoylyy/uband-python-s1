# -*- coding: utf-8 -*-
# author: shuan

import codecs
import os

def word_split(words):
	word_list = []
	for word in words:
		wd = word.split('-')
		word_list.extend(wd)
	return word_list

def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        wd = word_split(words)
        word_list.extend(wd)
    return word_list

def read_files(file_paths):
	final_word = []
	for file_path in file_paths:
		final_word.extend(read_file(file_path))
	return final_word


def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '') 
    return word.lower()

def format_words(words):
	words_list= []
	for word in words:
		wd = format_word(word)
		if wd == '':
			del wd
		else:
			words_list.append(wd)
	return words_list

def statistics(words):
	dictionary={}
	for word in words:
		if dictionary.has_key(word):
			dictionary[word] = dictionary[word]+1
		else:
			dictionary[word] = 1
	return dictionary

def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths

def sequence(dictionary):
	for item in dictionary:
		new_dict = sorted(dictionary.items(), key = lambda d:d[1], reverse = True)
	return new_dict




def main():
   
    # 读取文件
    rf = read_files(get_file_from_folder('data2'))
    print '获取了未格式化的单词%d个'%(len(rf))

    # 清洗文本
    rf_format = format_words(rf)
    print '获取了格式化的单词%d个 '%(len(rf_format))

    # 统计和筛选 
    sta = statistics(rf_format)
 
    # 排序
    # final_word = sequence(sta)
   
    
    # 输出文件
    print_to_csv(sta, 'output/test.csv')

if __name__ == "__main__":
    main()
 