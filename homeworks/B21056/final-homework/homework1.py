# -*- coding: utf-8 -*-


import codecs#引入codecs类
import os#引入os类print str.split( );
import operator
#1.读取文件
#['aa','aaa-bbb-sds']->['aa','aaa','bbb','sds']
def word_split(words):
	new_list=[]
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst=word.split('-')
			new_list.extend(lst)
	return new_list

def read_file(file_path):
	f=codecs.open(file_path,'r',"utf-8")
	lines=f.readlines()

	word_list=[]

	for line in lines:
		line=line.strip()
		words=line.split(' ')
		words=word_split(words)#去掉-
		word_list.extend(words)
	return word_list

#读取文件夹里的所有文件
def get_file_from_folder(folder_path):
	file_paths=[]
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths


#读取多文件里的单词
def read_files(file_paths):
	final_words=[]
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#2.获取格式化之后的单词
def format_word(word):#格式化一个单词
	fmt='abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ-'
	for char in word:
		if char not in fmt:
			word=word.replace(char,'')
	return word.lower()

def format_words(words):#格式化多个单词
	word_list=[]
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#3.统计单词数据
#{'aa':1,'bb':1}
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
	#words=read_file('data1/dt01.txt')
	words=read_files(get_file_from_folder('data2'))
	print '获取了未格式化的单词 %d 个 '%(len(words))
	#2.清洗文本
	f_words= format_words(words)
	#print '获取了已经格式化的单词 %d 个 '%(len(f_words))
	#print f_words

	#3.统计单词和排序
	word_dict=statictcs_words(f_words)

	#sorted_dict=sorted(word_dict.items(),key = operator.itemgetter(1))
	#↑是网上查的方法，发现这样字典会变成列表，输出函数print_to_csv又会报错，LIST没有key,我没有实现排序。
	#print sorted_dict
	#4.输出文件
	print_to_csv(word_dict,'output/test.csv')

if __name__ == '__main__':
    main()
