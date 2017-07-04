#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: huafeng
# data1测试作业

import codecs
import os
import collections

#1.读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()    # 读文件每行
    word_list = []
    for line in lines:
        line = line.strip()       # 去掉单词左右的空格
        words = line.split(" ")   # 用空格来分割单词。
        word_list.extend(words)   #在列表中增加分割的单词字符，索引位增加
    return word_list

#2.获取格式化的单个单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')  # 用空格代替 char字符
    return word.lower()  

#2.1.对所有单词进行循环格式化
def format_words(words):
  word_list = []
  for word in words:
    wd = format_word(word)
    if wd:
      word_list.append(wd)  # 在word_list中增加已格式化的单词列表，只占索引位
  return word_list
#3.统计单词数量
# {'aa':1 在的话 值+1，不在下一个}
def statictcs_words(words):
  s_word_dict = {}
  for word in words:
    if ( word in s_word_dict.keys()):
      s_word_dict[word] += 1
    else :
      s_word_dict[word] = 1
  return s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():       #格式化单词
  #1. 读取文本
  words = read_file('data1/dt01.txt')
  print (words)
  print ('获取了未格式化的单词 %d 个' % (len(words)))
  #2.清洗文本
  f_words = format_words(words)
  print(f_words)
  print('获取了格式化的单词 %d 个' % (len(f_words)))
  
  #3.统计单词
  word_dict = statictcs_words(f_words)

  #4.输出文件
  print_to_csv (word_dict,'data1/output1.csv')


if __name__ == '__main__':
  main()
