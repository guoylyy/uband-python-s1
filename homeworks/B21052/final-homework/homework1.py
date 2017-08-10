# -*- coding: utf-8 -*-

import codecs
import os


def word_split(words): 
    new_list=[]
    for word in words:
        if '-' not in word: 
            new_list.append(word) 
        else:
            lst=word.split('-')
            new_list.extend(lst) 
    return new_list 

#1. 读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(' ')
        words = word_split(words)
        word_list.extend(words)
    return word_list

#2获取格式化后的单词
def format_word(word):
    fmt ='abcdefghijklmnopqrstuvwxyz-'
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

#3统计单词数目
def statistic_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    return s_word_dict

#输出文件
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path, 'w+')
    for key in volcaulay_map.keys():
        value = volcaulay_map[key]
        nfile.write("%s, %s\n"%(key, value))
    nfile.close()

def main():
    #读取文件
    words = read_file('data1/dt01.txt')
    print 'Get %d unformatted words'% (len(words))
    #清洗单词
    f_words = format_words(words)
    print 'Get %d format words'% (len(f_words))
    #统计单词和排序
    word_dict = statistic_words(f_words)
    #输出文本
    print_to_csv(word_dict, 'output/data1-test.csv')


if __name__ == '__main__':
    main()