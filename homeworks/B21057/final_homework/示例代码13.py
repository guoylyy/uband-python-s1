# -*- coding: utf-8 -*-

# 读取文件~~~~~~~~放到主程序里面运行
# dsadada

import codecs
import os

def read_file(file_path):    
    f = codecs.open(file_path, 'r', "utf-8")                                               
    lines = f.readlines()                          
    
    word_list=[] #在这里添加个新列表 word_list，用于存放遍历出来的单词

    for line in lines:
        line = line.strip()                          
        words = line.split(' ')
           
        word_list.extend(words) #extend函数的意思就是(用新列表扩展原来的旧列表)
        						#这里把words里面的列表单词添加到word_list这个空白列表里面
    							#再次重复遍历单词
    return word_list #直到lines没有可以遍历的大东西了，返回 word_list 给read_file函数

def main():
    
    words=read_file('data1/dt01.txt') #调用read_file函数的结果 word_list 并赋值words
    
    print words # 打印 read_file 函数的结果 word_list
    print'一共有%d个单词'%(len(words)) # 用 len函数可以看到总数

if __name__ == '__main__':
    main()