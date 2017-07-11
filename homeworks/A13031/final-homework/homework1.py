# -*- coding: utf-8 -*-

import codecs
import os
#1. 读取文件
#去除斜杠
def word_split(words):
  new_list  = []
  for word in words:
    if '-'  not in  word:
      new_list.append(word)
    else:
      lst  =  word.split('-')
      new_list.extend(lst)    
  return  new_list

def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip() #除去左右两边空格
        words = line.split(" ") #按空格分割
        words = word_split(words)  #用-分割
        word_list.extend(words)
    return  word_list

def get_file_from_folder(folder_path):
  file_paths  = []
  for root, dirs, files in os.walk(folder_path):
      for file in files:
          file_path = os.path.join(root, file)
          file_paths.append(file_path)
  return  file_paths

#读取多文件里的单词
def read_files(file_paths):
  final_words = []
  for path in file_paths:
    final_words.extend(read_file(path))
  return  final_words

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
  word_list = []
  for word in words:
      wd= format_word(word)
      if wd:
        word_list.append(wd)
  return  word_list      

#3.统计单词数目
def statictcs_words(words):
  s_word_dict = {}
  for word in words:
    if s_word_dict.has_key(word):
      s_word_dict[word] = s_word_dict[word] + 1
    else:
      s_word_dict[word] =1
  return  s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():
  #1.读取文本
  #word  =  read_file('data1/dt01.txt')
  paths  =  get_file_from_folder('data2')
  words	=	read_files(paths)
  print	'获得了未格式化的单词%d个	'	%	(len(words))
  #2.清洗文本
  f_words=  format_words(words)
  print '获取了已经格式化的单词%d个 ' % (len(f_words))
  
  #3.统计单词和排序
  word_dic= statictcs_words(f_words)
  print  sorted(word_dic.items(),key=lambda item:item[1],reverse=True) #可输出，但是输出后可能因路径权限发生：IOError: [Errno 13] Permission denied: 'output/test.csv'错误，以管理员身份获取所有权限后可解决
  #4.输出文件
  print_to_csv(word_dic,'output/test.csv')

if __name__ == "__main__":
    main()
