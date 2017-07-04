# -*- coding: utf-8 -*-

import codecs
import os

#
# 程度较好的同学可以不看 tips.py
#

#--===========================
#
#--===========================

#1. 读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        print words

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

#3.读取文件夹里的所有文件
def get_file_from_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print file_path


#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():
    #1. read file
    read_file('data1/dt01.txt')
    #2. format word
    print format_word(' make  ')
    print format_word('  kill-a')
    #3. get files
    get_file_from_folder('data2')
    #4. 输出成csv
    volcaulay_map = {
        'see': 1024,
        'make':222
    }
    print_to_csv(volcaulay_map, 'output/test.csv')


if __name__ == '__main__':
    main()