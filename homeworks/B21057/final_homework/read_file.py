# -*- coding: utf-8 -*-

# 读取文件~~~~~~~~
# 
import codecs #读取文件并返回Unicode
import os #Python的系统编程的操作模块，可以处理文件和目录
import datetime

def read_file(file_path):
  f = codecs.open(file_path,'r','utf-8')
  lines = f.readlines()
  word_list=[]
  for line in lines: 
    line = line.strip()
    words = line.split(' ') 
    word_list.extend(words)
    print words
  return words

def main():
  read_file('data1/dt01.txt')
  
if __name__ == '__main__':
  main()


