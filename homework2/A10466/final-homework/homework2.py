# -*- coding: utf-8 -*-
#读取文本-清洗文本-排序-输出文本


import codecs
import os
import collections

def word_split(words):
    new_list=[]
    for word in words:
        if '-'not in word:
            new_list.append(word)
        else:
            lst=word.split('-')
            new_list.extend(lst)
    return new_list

#读取文本
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list=[]
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        words = word_split(words)
        word_list.extend(words)
    return word_list

def get_file_from_folder(folder_path):
    file_paths=[]
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def read_files(file_paths):
    final_words=[]
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words


#清洗文本
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
    word_list=[]
    for word in words:
        word_list.append(format_word(word))
    return word_list

#统计单词数目
def statistic_words(words):
    s_word_dict={}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word]=s_word_dict[word]+1
        else:
            s_word_dict[word]=1
    return s_word_dict

 #字典排序
def sort_by_count(d):
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()




def main():
    words=read_files(get_file_from_folder('data2'))
    print '获取了未清洗的文件%d'%(len(words))
    #print words

    f_words=format_words(words)
    print '获取了已经格式化的单词%d'%(len(f_words))
    #print f_words

    word_dict= statistic_words(f_words)
    sorted_word_dict=sort_by_count(word_dict)
    print_to_csv(sorted_word_dict,'output/test.csv')


if __name__ == '__main__':
    main()