# -*- coding: utf-8 -*-
import codecs
import os

##读取文件夹里的所有文件
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


#1. 读取文件
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            list = word.split('-')
            new_list.extend(list)
    return new_list


def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines() 
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ") 
        words = word_split(words)
        word_list.extend(words)
    return word_list

def read_files(file_paths):
    final_words = []
    for path in file_paths:        
        final_words.extend(read_file(path))
    return final_words


#2.获取格式化之后的单词 (小写化)
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
    word_f = []
    for word in words:
        wd =  format_word(word)
        if wd:
            word_f.append(wd)
    return word_f

def count(words):
    dict_words = {}
    for word in words:
        if dict_words.has_key(word):
            dict_words[word] = dict_words[word] + 1
        else:
            dict_words[word] = 1
    return dict_words
    

#3.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        #向文件中写入指定字符串
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():
    #1. read file
    # word_1 = read_file('data1/dt02.txt')
    paths = get_file_from_folder('data2')
    # print paths
    word_1 = read_files(paths) 
    print '%d' %(len(word_1))
    print '清洗中ing'
    
    #2. format word
    word_lower = format_words(word_1) 
    print '%d' %(len(word_lower))

    #3.统计单词数
    counted =  count(word_lower)

    #4.输出csv
    print_to_csv(counted,'output/test.csv')


if __name__ == "__main__":
    main()
