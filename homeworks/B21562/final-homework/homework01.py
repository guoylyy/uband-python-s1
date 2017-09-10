# -*- coding: utf-8 -*-
import codecs #引入 codecs 类
import os #引入 os 类
import collections


#1. 读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")  # 打开路径里的文件
    lines = f.readlines() #按行来读取
    word_list=[] #要能够在主程序里使用刚刚读取并分割的单词，不能直接打印出来，而是应该把它存储到一个list变量里
    for line in lines: #对每一行做循环
        line = line.strip()	#去掉每一行两侧的空格
        words = line.split(" ")	#并按照空格来区分单词
        words=word_split(words) #按照连接符再分一次单词
       # print words
        word_list.extend(words)#把区分出来的单词加入到word_list中，注意，这里写append会报错，因为生成的words是多个单词组成的列表，应该使用extend
    return word_list
def word_split(words): #再用其他方法分割单词
	new_list=[]
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst=word.split('-') #将用连接符链接的单词区分开
			new_list.extend(lst)
	return new_list
#2.获取格式化之后的单词
def format_word(word):  #格式化一个单词
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word: #对于单词中的每一个字符
        if char not in fmt: #如果它不在fmt字符串中，即不是小写的英文字母
            word = word.replace(char, '') #就把单词中的这个字符替换为空格
    return word.lower() #最后把单词中的所有字符换成小写

def format_words(words): #通过循环命令，来格式化所有的单词,并且还需要把空单词删掉
	#format_word_list=[]
	word_list=[]
	for word in words: #对words列表中的所有单词
		#format_word(word) #全部格式化
		#format_word_list.append(word) #格式化之后加入到format_word_list列表中，可以简化为format_word_list.append(format_word(word))
		wd=format_word(word)#在这里先把之前格式化的每一个单词赋值给wd
		if wd: #再判断wd是不是一个空单词
			word_list.append(format_word(word)) #如果不为空，才把它加入到列表里，这时候，列表里就没有空单词了
	return word_list

#3.统计单词数目
#使用字典来统计单词{'aa':1,"bb":5}
def statictcs_words(words):
	s_word_dict={}
	for word in words:
		if s_word_dict.has_key(word): #当字典里有了这个单词，第二次再遇到时，就对键值+1
			s_word_dict[word]=s_word_dict[word]+1 #通过方括号来访问字典里每一个键的值，[word]表示键，冒号前面的部分，s_word_dict[word]表示值，冒号后的数字
		else:
			s_word_dict[word]=1 #一开始是一个空字典，第一次遇到某个单词时，运行这一句，为这个单词表示的键赋值为1
	
	return s_word_dict

#4.对统计后的单词排序
def sort(s_word_dict):
	from collections import OrderedDict #这里需要使用一个collections模块，用来生成有序字典
	word_sort_dict=OrderedDict(sorted(s_word_dict.items(), key=lambda x: x[1],reverse=True))
	#sorted命令用来给字典排序，但排序之后输出的结果不是字典，而是列表
	#于是加上一个命令，把生成的列表变成一个有序字典
	#for k,v in word_sort_dict.items():
	#	print k,v
	return word_sort_dict

#4.输出字典文件到csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()
#5.输出排序结果到csv
def printsort_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for index,number in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()

def main():
    #1. read file
    
    #word_list=read_file('data1/dt01.txt') #必须要加上这句话，传递了word_list之后，才能正确地打印
    #print word_list #虽然前面return了word_list，但是在这里直接打印word_list还是会报错，原因是没有传递过来
    words=read_file('data1/dt01.txt') #也可以给word_list改名words后传递过来，和上面是一样的
    print words 
    print "获取了未格式化的单词%d个"%(len(words))
    #2. format word
    fwords=format_words(words)
    print "获取了已经格式化的单词%d个" %(len(fwords))
    print fwords
    #3. 统计文件
    s_word_dict=statictcs_words(fwords)
    print s_word_dict
    sortdict=sort(s_word_dict)
    #4.输出文件
    print_to_csv(sortdict, 'output/output01.csv')#输出文件这里，括号里逗号前是需要输出的结果变量，括号后是输出的路径


if __name__ == '__main__':
    main()
