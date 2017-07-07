# -*- coding: utf-8 -*-
import codecs 
import os
#1. 读取文件
def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")
		words = word_split(words)
		word_list.extend(words)
	return word_list

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
#['aa-bb-cc'] => ['aa','bb','cc']
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

def format_word(word):
	fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()    

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
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict

#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
	nfile = open(to_file_path,'w+')
	for key in volcaulay_map.keys():
		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()

def sort():
	f=open('output/test1.csv')
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
	g=open('output/test2.csv','w+')
	for i in range(0,len(cc)):
		g.write(cc[i][0] + "\n") # 把列表内容按照一定顺序写入新的文件
	g.close()

def main():
	print '读取文件......'
	#1. 读取文本
	paths = get_file_from_folder('data2')
	words = read_files(paths)
	print '获取了未格式化的单词 %d 个' % (len(words))
	print '清洗文本......'
	#2. 清洗文本
	f_words = format_words(words)
	print '获取了已格式化的单词 %d 个' % (len(f_words))

	#3. 统计单词和排序
	#print statistics_words(f_words)
	word_dict = statistics_words(f_words)
	print '输出文件test1.....'
	#4. 输出文件
	print_to_csv(word_dict, 'output/test1.csv')
	print '输出文件test2......'
	#5. 排序
	sort()
	
if __name__ == '__main__':
	main()