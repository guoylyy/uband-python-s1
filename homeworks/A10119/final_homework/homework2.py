# -*- coding: utf-8 -*-

import codecs
import os
import csv

#1. 读取文件
#['aa', 'aaa-bbb-sss'] => ['aa','aaa','bbb','sss']
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
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()#把空行去掉
        words = line.split(" ")#分词,用空格分割
        words = word_split(words)#用-分割
        word_list.extend(words)
    return word_list

#3.读取文件夹里的所有文件
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

#读取多文件里的单词
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words


#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#统计单词数目
#('aa':4,'bb':1)
def statictcs_words(words):#给它一个参数words，并接受传递过来的单词组f_words
	s_word_dict = {}#这里设置一个字典
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1#这里可以理解为，字典是无序的，通过键来找到关联值。
                                #这里s_word_dict[word]对于出现一次以上的单词键的值返回的应该都是None，遍历之后不断在原基础上加1，
                                #相当于一个计数的作用了，而只出现一次的单词相当于不存在的键，会出现KeyError，所以直接给定1。
	return s_word_dict

#4.输出成csv

    
# def print_to_csv(volcaulay_map, to_file_path):
#     nfile = open(to_file_path,'w+')
#     for key in volcaulay_map.keys():
#         val = volcaulay_map[key]
#         nfile.write("%s,%s\n" % (key, str(val)))
#     nfile.close()

def main():
    #读取文本
    # words = read_file('data1/dt01.txt')
    # paths = get_file_from_folder('data2')
    # words = read_files(['data2/2016.01.02.TXT', 'data2/2016.01.09.TXT'])
    words = read_files(get_file_from_folder('data2'))

    print '获取了未格式化的单词 %d 个 ' %(len(words))

    # #清洗文本
    f_words = format_words(words)
    print '获取了已经格式化的单词 %d 个 '% (len(f_words))

    # #统计单词和排序
    word_dict = statictcs_words(f_words)

    # #排序
    dict = sorted(word_dict.iteritems(), key=lambda d:d[1], reverse = True)
    # sorted_word_dict = sorted(word_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    # sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1))
    # word_dict = sorted_word_dict
    # print dict
    with open('output/test.csv', 'wb') as csvfile:#排序+输出文件
        fwriter = csv.writer(csvfile)
        for x in dict:
            fwriter.writerow(x)


    # #4输出文件
    # print_to_csv(dict, 'output/test.csv')


if __name__ == "__main__":
    main()
