# -*- coding: utf-8 -*-

import codecs
import os

def read_file(file_path): 
    f = codecs.open(file_path, 'r', "utf-8") 
    lines = f.readlines() 
    word_list=[] 
    for line in lines: 
        line = line.strip() 
        words = line.split(' ') 
        word_list.extend(words) 
    return word_list  

def format_word(word): #得到从 format_words 传过来的参数，并传递出去
	fmt='abcdefghijkmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word=word.replace(char,'') # fmt里面没有的就用空格代替
	return word.lower()  #换成小写，返回 word 给 format_words

def format_words(words): #接受 参数 和传出参数
    word_list=[] #我们新建了一个列表word_list

    for word in words: #对words(为格式化的单词组)遍历
        wd=format_word(word) #1、将 word 传到 format_word 函数
                             #2、得到从format_word返回的word并给它一个变量名 wd
        if wd: #if wd的意思是如果wd没有东西则不执行，有的话执行语句
            word_list.append(wd) #把单词添加到 word_list (判断wd有单词，添加到word_list)
    return word_list #返回 word_list 函数并循环

def main(): 
    words=read_file('data1/dt01.txt') 
    print'获取了%d个未格式化的单词 '%(len(words)) #打印未格式化的单词数目
    print words #打印未格式化的单词
    
    f_words=format_words(words) #把未格式化的单词组 words 传到 format_words 代码块
                                #接受已经格式话的单词 并组成列表，给它们变量名 f_word
    print'获取了已经格式化的单词%d个 '%(len(f_words)) #检测 f_word 的数量
    print f_words #打印已经格式化的单词
if __name__ == '__main__':
    main()