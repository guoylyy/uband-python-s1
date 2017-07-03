# -*- coding: utf-8 -*-

import codecs
import os

#1. 读取文件&分割单词
#分割单词之去掉横杠
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
    f = codecs.open(file_path, 'r', "utf-8") #打开
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip() #去掉空格
        words = line.split(" ") #用空格分割
        words = word_split(words) #用-分割
        word_list.extend(words)
    return word_list

#读取文件夹里的多文件
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#读取文件夹里的所有文件
def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
	    for file in files:
	        file_path = os.path.join(root, file)
	        file_paths.append(file_path)
	return file_paths

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()
#  获取格式化之后的单词list
def format_words(words):
    word_list = []
    for word in words:
        wd = format_word(word)
        if wd:
            word_list.append(wd)
    return word_list

#3.统计
def count_word(words):
    word_amount = {}
    for word in words:
        if word_amount.has_key(word):
            word_amount[word] = word_amount[word] + 1
        else:
            word_amount[word] = 1
    return word_amount
        
#5.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def main():
    #读取文件&分词
    words = read_files(get_file_from_folder('data2'))
    print '获取了未格式化的单词 %d 个' % (len(words))
    #格式化
    f_words = format_words(words)
    print '获取了格式化的单词 %d 个' % (len(f_words))
    #统计
    word_dict = count_word(f_words)
    #输出
    print_to_csv(word_dict, 'output/homework1.csv')
    

if __name__ == "__main__":
    main()
