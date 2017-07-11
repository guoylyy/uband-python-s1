# -*- coding: utf-8 -*-

import codecs
import os


#读文件

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
        lint = line.strip()  #把左右的空格去掉
        words = line.split(" ")  #用空格分割  一定得在中间打个空格
        words = word_split(words)
        word_list.extend(words)
    return word_list

# 格式化单词

def format_word(word):
    fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):    #搞个函数让这个格式针对全部的单词
    word_list = []
    for word in words:    #也就是整个循环跑一次 用for
        wd = format_word(word)
        if wd:
            word_list.append(format_word(word))    #在词尾添加新对象
    return word_list

#统计数据
def statistics_word(words):
    s_word_dic = {}
    for word in words:
        if s_word_dic.has_key(word):
            s_word_dic[word] = s_word_dic[word] + 1
        else:
            s_word_dic[word] = 1
    return s_word_dic

#输出成csv
def print_to_csv(vocabulary_map, to_file_path):
    nfile = open(to_file_path, 'w+')
    for key in vocabulary_map.keys():
        val = vocabulary_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def main():
    #读文本
    words = read_file('data1/dt01.txt')   #读取data1的dt01
    # print words
    print '获取了未格式化的单词 %d 个' % (len(words))

    #洗文本
    f_words = format_words(words)
    print '获取了已格式化的单词 %d 个' %(len(f_words))

    #统计数据
    word_dict = statistics_word(f_words)
    # print word_dict
    #输出文本
    print_to_csv(word_dict, 'output/testdata1.csv')


if __name__ == "__main__":
    main()
