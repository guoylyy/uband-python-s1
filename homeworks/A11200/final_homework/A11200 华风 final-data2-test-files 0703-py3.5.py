#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: huafeng
# data2作业

import codecs
import os
import collections

#1.读取文件
def word_split(words):
  new_list = []
  for word in words :
    if '-' not in word:
      new_list.append(word)
    else :
      lst = word.split('-')
      new_list.extend(lst)
  return new_list 

def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()    # 读文件每行
    word_list = []
    for line in lines:
        line = line.strip()       # 去掉单词左右的空格
        words = line.split(" ")   # 用空格来分割单词。
        words = word_split(words)   # 用-来分割单词。
        word_list.extend(words)   #在列表中增加分割的单词字符，索引位增加
    return word_list
#读取多个文件名    
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):    # 路径中 根目录，文件夹，文件。
        for file in files:
            file_path = os.path.join(root, file)    # 路径在 全路径中 
            file_paths.append(file_path)
    return file_paths


#读取很多文件的单词
def read_files(file_paths):
  final_words = []
  for path in file_paths:
    final_words.extend(read_file(path))
  return final_words

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
  # words = read_file('data1/dt02.txt')
  # print (words)
  words = read_files(get_file_from_folder('data2'))
  print ('获取了未格式化的单词 %d 个' % (len(words)))
  #2.清洗文本
  f_words = format_words(words)
 
  print('获取了格式化的单词 %d 个' % (len(f_words)))

  #3.统计单词
  word_dict = statictcs_words(f_words)

  #4.输出文件
  print_to_csv (word_dict,'data1/output3.csv')


if __name__ == '__main__':
  main()
