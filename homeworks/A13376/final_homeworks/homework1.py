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
			list = word.split('-')
			new_list.extend(list)
	return new_list


def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    #读取行，输出为列表
    #保存在lines里
    lines = f.readlines() 
    word_list = []
    for line in lines:
    	#用于移除字符串头尾指定的字符（默认为空格）
        line = line.strip()
        #通过指定分隔符（默认为所有的空字符）对字符串进行分割
        #输出为列表保存在words里
        words = line.split(" ") 
        words = word_split(words)
        word_list.extend(words)
    return word_list

#2.获取格式化之后的单词 (小写化)
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
	word_f = []
	for word in words:
		wd =  format_word(word)
		if wd:
			word_f.append(wd)
	return word_f

def count(words):
	dict_words = {}
	for word in words:
		if dict_words.has_key(word):
			dict_words[word] = dict_words[word] + 1
		else:
			dict_words[word] = 1
	return dict_words
	

#3.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        #向文件中写入指定字符串
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():
    #1. read file
    word_1 = read_file('data1/dt02.txt') #用word_1来接收一个列表
    print '%d' %(len(word_1))
    
    #2. format word
    word_lower = format_words(word_1) #用word_lower来接收已经格式化的列表
    print format_words('aa 134dsa')
    print '%d' %(len(word_lower))

    #3.统计单词数
    counted =  count(word_lower)
    print counted

    #4.输出csv
    print_to_csv(counted,'output/test.csv')


if __name__ == "__main__":
    main()
