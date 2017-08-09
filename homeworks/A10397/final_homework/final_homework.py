#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

import codecs #引入 codecs 类
import os #引入 os 类

#1. 读取文件
#['aa', 'aaa-bbb-ccc']=>['aa','aaa','bbb','ccc']
def word_split(words):
	new_list=[]
	for word in words:
		if '-' not in word: # 如果 - 不在words执行
			new_list.append(word) #添加word到new_list
		else:
			lst=word.split('-') #在的话split函数按 - 分割单词
			new_list.extend(lst) #extend函数用旧列表lst替换新列表 new_list
	return new_list #返回结果 new_list



def read_file(file_path): #给read_file函数一个参数file_path；file_path就是要打开的文件
	f = codecs.open(file_path,'r','utf-8') #codecs.open是一个打开文件的函数，赋值给f；
	                                         #file_path是要打开的文件；'r'是打开的方法：读取；'utf-8'是编码
	lines = f.readlines()#readline用于读取‘所有行’并返回列表；只需知道这个是读取文件的作用
	                      #赋予它一个变量名lines
	word_list=[] #在这里添加个新列表word_list，用于存放遍历出来的单词

	for line in lines:
		line = line.strip()
		words = line.split(' ')#用空格分割
		words = word_split(words)#用-分割
		word_list.extend(words) #extend函数的意思就是‘用新列表扩展原来的旧列表’
		                        #这里把words里面的列表单词添加到word_list这个空白列表里面
		                        #再次重复遍历单词

	return word_list #直到lines没有可以遍历的大东西了，返回 word_list 给read_file函数

#读取文件夹里的所有文件
def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths

           

#读取多文件里的单词
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#2.获取格式化之后的单词
def format_word(word): #给format_word赋予一个参数word，这个参数word就是我们输出的单词
	fmt='abcdefghijklmnopqrstuvwxyz-' #设置一个我们所需要单词的字符串

	for char in word: #对word遍历
		if char not in fmt: #判断char里面有没有fmt里面的单词，没有则执行下面的替换语句
			word=word.replace(char,'') #replace函数的作用是用新字符换旧字符，然后给一个变量word
			                           #这里意思是用后面的空格取代char，' '里面是空格

	return word.lower() #lower函数：把字符串全部换成小写，这里返回word给函数format_word


def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#3.统计单词数目
#{'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict={}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word]=s_word_dict[word]+1
        else:
            s_word_dict[word]=1
    return s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def main():
	#1.读取文本
	#words=read_file('data1/dt01.txt') #调用read_file函数的结果 word_list 并赋值words
	#print words # 打印 read_file函数的结果
	paths = get_file_from_folder('data2')
	
	words = read_files(paths)
	print '一共有%d个单词 '%(len(words)) #用len函数可以看到总数

	#2.清洗文本
	#print format_word('A2as') #假设我们把A2as传递过去，A和2是fmt没有的
	f_words = format_words(words)
	#print f_words
	print '已经格式化的单词 %d 个' %(len(f_words)) 

	#3.统计单词和排序
	#print statictcs_words(f_words)
	word_dict = statictcs_words(f_words)

	#4.输出文件
	print_to_csv(word_dict,'output/test.csv')



if __name__ == '__main__':
	main()