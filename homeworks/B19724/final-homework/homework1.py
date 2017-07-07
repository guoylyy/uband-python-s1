# -*- coding: utf-8 -*-
import codecs #用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode 
import os
#1. 读取文件
def read_file(file_path):
	f = codecs.open(file_path, 'r', 'utf-8') #文件名称/路径；打开模式r-只读，w-只写，r+读写
	lines = f.readlines() #读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
	word_list = []
	for line in lines:
		line = line.strip() #strip() 方法用于移除字符串头尾指定的字符（默认为空格）
		words = line.split(" ") #split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
		word_list.extend(words)
		#print word_list
	return word_list #重要
	
#2. 获取格式化之后的单词
def format_word(word):
	fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '') #字符替换
	return word.lower() #变小写

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#3. 统计单词数目
def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] =s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict

#4. 输出成csv
def print_to_csv(vocabulary_map, to_file_path):
	nfile = open(to_file_path, 'w+')
	for key in vocabulary_map.keys():
		val = vocabulary_map[key]
		nfile.write("%s, %s\n" %(key,str(val)))
	nfile.close()

def sort():
	f=open('output/test_1.csv')
	aa={}
	bb=[]
	k=[]
	for i in f.readlines():
		bb.append(i.split('\n'))   # 把文件内容读入列表
		k.append(i.split(',')[1])  # 把需要排下的列的内容加入到一个列表

	for i in range(0,len(bb)):
		aa[bb[i][0]]=int(k[i])  #生成一个字典，键是文件内容，值是需要排序的内容
	f.close()
	cc=sorted(aa.items(),key=lambda aa:aa[1])  # 对字典进行按照值来排序，返回值是个列表
	g=open('output/test_2.csv','w+')
	for i in range(0,len(cc)):
		g.write(cc[i][0] + "\n") # 把列表内容按照一定顺序写入新的文件
	g.close()
def main():
	#1. read file
	words = read_file('data1/dt01.txt')
	print '获取了未格式化的单词 %d 个' % (len(words))
	#2. format word
	f_words = format_words(words)
	print '获取了已格式化的单词 %d 个' % (len(f_words))
	#3. count words
	word_dict = statistics_words(f_words)
	#4. file	
	print_to_csv(word_dict, 'output/test_1.csv')
	#5. sort
	sort()

if __name__ == "__main__":
    main()
