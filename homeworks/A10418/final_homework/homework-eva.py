# -*- coding: utf-8 -*-

import codecs
import os

#以-为切分符号，将单词切分开来
def word_split(words): #接受从read_file传过来的words[也就是说，其实函数的引用是无所谓先后的，先写的函数也可以引用后面的函数的变量]
	new_list=[]
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst=word.split('-')
			new_list.extend(lst)#extend函数用旧列表 lst 替换新列表 new_list

		return new_list #返回结果 new_list

#读取单个文件
def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list=[]
	for line in lines:
		line = line.strip()
		words = line.split(' ')
		words = word_split(words) #将words传到word_split,接受返回的值
		word_list.extend(words)	
	return word_list

#读取文件夹里的所以文件
def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root,file)
			file_paths.append(file_path)

	return file_paths

#读取多个文件
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#格式化单个单词
def format_word(word):
	fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word=word.replace(char,'')
	return word.lower()

#格式化所有单词-遍历
def format_words(words):
	word_list = []

	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#统计单词出现频率
def statistcs_words(words):
	s_word_dict={}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word]=s_word_dict[word]+1
		else:
			s_word_dict[word]=1
	return s_word_dict

#输出
def print_to_csv(volcabulary_map,to_file_path):
	nfile=open(to_file_path,'w+') #to_file_path是地址，‘w+’是写入方式，给变量名nfile
	for key in volcabulary_map.keys():
		values=volcabulary_map[key]
		nfile.write("%s,%s\n"%(key,values)) #\n表示换行

	nfile.close()


def main():
	#words=read_file('data/2016.01.02.txt')
	words = read_files(get_file_from_folder('data'))
	f_words=format_words(words)
	word_dict=statistcs_words(f_words)

	print_to_csv(word_dict,'output/test.csv')#将word_dict这个统计过后的单词组传递到print_to_csv
											#将要生成的文件的地址写入，output/test.csv写入并传递

if __name__ == "__main__":
    main()
