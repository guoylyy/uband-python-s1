# -*- coding: utf-8 -*-
#blueprint 1读取 2处理 3统计 4输出

import codecs
import os

def read_file(folder_path):
    list1 = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            list1.append(file_path)
    return list1

def format_word(word):
    word = word.lower()
    fmt = "abcdefghijklmnopqrstuvwxyz-'"
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word

def process_word(list1):
    dict1 = {}
    for raw_word in list1:
        f = codecs.open(raw_word, 'r', "utf-8")
        lines = f.readlines()   
        for line in lines:
            line = line.strip()
            word = line.split(" ")     
            for word1 in word:
                word1 = format_word(word1)
                if dict1.has_key(word1):
                    dict1[word1] += 1
                else:
                    dict1[word1] = 1

    del dict1['']
    list2 = []
    list2 = sorted(dict1.items(),key=lambda dict1: dict1 [1],reverse=False) 
    return list2 


def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for item in volcaulay_map:
        nfile.write("%s,%s\n" % (item[0], item[1]))
    nfile.close()
          
def main(): 
    list1 = read_file('data1')
    list2  = process_word(list1)   
    print_to_csv(list2, 'test.txt')
    
    
if __name__ == "__main__":
    main()
   
