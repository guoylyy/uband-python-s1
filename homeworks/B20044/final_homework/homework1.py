# -*- coding: utf-8 -*-

import codecs   #漏了
import os


def word_split(words):   #_打成了-
	word_list=[]
	for word in words:
		if '-' not in word:
			word_list.append(word)
		else:
			lst=word.split('-')
			word_list.extend(lst)
	return word_list
	


#1. 读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()

    word_list=[]

    for line in lines:
        line = line.strip()
        words = line.split(" ")

        words=word_split(words)  #word_split打成了word.split

        word_list.extend(words)
    return word_list

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ--'

    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
	word_list=[]
	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
	return word_list



def statis_words(words):
	dic={}
	for word in words:
		if dic.has_key(word):
			dic[word]=dic[word]+1
		else:
			dic[word]=1
	return dic

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():
    words=read_file('data1/dt01.txt')
    print "获取了未格式化的单词%d个 "%(len(words))

    # print format_word('make123')
    f_words=format_words(words)
    print f_words
    print'获取了格式化后的单词%d 个'%(len(f_words))

    sw=statis_words(f_words)
    print_to_csv(sw, 'output/test homework1.csv')

    

if __name__ == "__main__":
	main()
    


