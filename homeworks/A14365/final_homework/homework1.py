# -*- coding: utf-8 -*-

import codecs
import os




#0.读取文件夹里的所有文件
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print file_path
            file_paths.append(file_path)
    return file_paths




#1. 读取单个及多个文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ") #按照空格分割单词
        words = word_split(words) #按照‘-’分割
        word_list.extend(words)
    return word_list

def read_files(file_paths):
    final_words = []
    for path in file_paths:
      final_words.extend(read_file(path))
    return final_words

#2.清洗文件

#2.1获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
    lst = []
    for word in words:
      wd = format_word(word)
      if wd:
        lst.append(format_word(wd))
    return lst

#2.2获取格式化之后的单词
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            lst = word.split('-')
            new_list.extend(lst)
    return new_list

#3.统计计数
def count_word(words):
    counts = dict()
    for word in words:
      if word not in counts:
        counts[word] = 1
      else :
        counts[word] += 1
    #print counts

    return counts

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for list_item in volcaulay_map:
        
        nfile.write("%s,%s\n" % (list_item))
    nfile.close()



def main():

#1.读入文件和分割单词
        
    word_1 = read_files(get_file_from_folder('data2'))
 
    #word_1 = read_file('data1/dt01.txt')
    #print word_1
    print '获取了未知格式的单词%d个' %(len(word_1))
#2.清洗文本
    
    f_words = format_words(word_1)
    print '获取了已经格式化的单词%d个 ' %(len(f_words))
    
    #print '获取了已经格式化的单词%d个'  %(len(f_words))
#统计单词
    counts = count_word(f_words)
#排序
    counts_1 = sorted(counts.items(), key=lambda d:d[1], reverse = True)
    #print counts_1
    # #输出
    print_to_csv(counts_1,'output/test.csv')



if __name__ == "__main__":
    main()
