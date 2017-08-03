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

def format_word(word): #给format_word赋予一个参数word，这个参数 word就是我们输出的单词
	fmt='abcdefghijkmnopqrstuvwxyz-' #设置一个我们所需要单词的字符串
	
	for char in word: #对word遍历
		if char not in fmt: #判断char里有没有 fmt 里面的单词,没有则执行下面的替换语句
			word=word.replace(char,'') #replace函数的作用是用新字符换旧字符,然后给一个变量word
									   #这里是意思是用后面的空格取代char，' '里面是空格
	
	return word.lower() #lower函数的意思把字符串里全部换小写，这里返回 word 给函数 format_word

def main(): 
    words=read_file('data1/dt01.txt') 

    print format_word('A2as') #假设我们把A2as传递过去，A和2是fmt没有的，你觉得会打印出什么

if __name__ == '__main__':
    main()