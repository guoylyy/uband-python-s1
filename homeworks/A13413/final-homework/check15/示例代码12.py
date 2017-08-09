# -*- coding: utf-8 -*-

# 读取文件~~~~~~~~

import codecs #引入 codecs 类
import os #引入 os 类

def read_file(file_path): #给read_file函数一个参数file_path;file_path就是你要打开的文件
    
    f = codecs.open(file_path, 'r', "utf-8") #cpdecs.open是一个打开文件的函数，赋值给f；
                                             #file_path是要打开的文件;'r'是打开的方法：读取; "utf-8"是编码   
    lines = f.readlines() #readlines用于读取 所有行 并返回列表，你只用知道这个是读取文件的作用
                          #赋予它一个变量名lines
    
    for line in lines: #对lines遍历
        line = line.strip() #strip()这个函数的意思移除整个字符串头尾指定的字符
                            #strip()默认为空格,因为()里面什么也没有，这里移除整个字符串前后空格
        
        words = line.split(' ') #split()函数用与分割字符,默认空格，按空格分割
                                
        print words #输出得到的单词，再次遍历

    return words #返回words

def main():
    read_file('data1/dt01.txt') # 这里把文件的地址传到read_file函数

if __name__ == '__main__':
    main()