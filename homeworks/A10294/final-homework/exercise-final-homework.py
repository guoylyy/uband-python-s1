# -*- coding: utf-8 -*-

import codecs
import os

#读取文件
def read_file(file_path):
  f = codecs.open(file_path, 'r', "utf-8")  #打开文件
  lines = f.readlines()
  word_list = []
  for line in lines:
    line = line.strip()  #去空格
    words = line.split(" ")   #用空格分割
    word_list.extend(words)
  return word_list

#分词,获得格式化后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
  word_list = []
  for word in words:
    word = format_word(word)
    if word:
      word_list.append(format_word(word))
  return word_list

#统计单词
def allwords(words):
  allwords_dict = {}
  for word in words:
  	if allwords_dict.has_key(word):
  		allwords_dict[word] = allwords_dict[word] + 1
  	else:
  		allwords_dict[word] = 1
  return allwords_dict


#排序
def sorted_words():
	sorted_words = sorted(volcaulay_map.items(),key=lambda item:item[1],reverse=True)
#输出
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()



def main():
  #读取文件
  words = read_file('data1/dt01.txt')
  # 格式化单词
  print '获取了%d 个未格式化单词'%(len(words))
  f_words = format_words(words)
  print '已经格式化的单词%d '%(len(format_words(words)))
  #
  volcaulay_map = allwords(f_words)
  print_to_csv(volcaulay_map, 'output/test.csv')

  #排序
  print sorted(volcaulay_map.items(),key=lambda item:item[1],reverse=True)
  



if __name__ == '__main__':
    main()