# -*- coding: utf-8 -*-

import codecs
import os

#读取文件
def word_split(words):   #去除单词里的-
  word_list2 = []
  for word in words:
    if '-' not in word:
      word_list2.append(word)
    else:
      list = word.split('-')
      word_list2.extend(list)
    return word_list2
#读取文件
def read_file(file_path):
  f = codecs.open(file_path, 'r', "utf-8")  #打开文件
  lines = f.readlines()
  word_list = []
  for line in lines:
    line = line.strip()  #去空格
    words = line.split(" ")   #用空格分割
    words = word_split(words)
    word_list.extend(words)
  return word_list

#读取文件夹里的所有文件
def get_file_from_folder(folder_path):
  file_paths = []
  for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
  return file_paths
#读取多个文件里的单词
def read_files(file_paths):
  final_words = []
  for path in file_paths:
    final_words.extend(read_file(path))
  return final_words

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


#输出
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():
  
  words = read_files(get_file_from_folder('data2'))

  # 格式化单词
  print '获取了%d 个未格式化单词'%(len(words))
  
  f_words = format_words(words)
  print '已经格式化的单词%d '%(len(format_words(words)))
  
  volcaulay_map = allwords(f_words)
  print_to_csv(volcaulay_map, 'output/test2.csv')
  print sorted(volcaulay_map.items(),key=lambda item:item[1],reverse=True)
if __name__ == '__main__':
    main()