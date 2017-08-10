# -*- coding: utf-8 -*-
import codecs
import os
import re #在菜鸟教程Python split的笔记里看到用这个可以用多种分割符就没再定义函数了_(:зゝ∠)_

#读取一个文件
#并把单词分割
def read_file(file_path): 
    f = codecs.open(file_path, 'r', "utf-8") 
    lines = f.readlines() 
    word_list=[] 
    for line in lines: 
        line = line.strip() 
        #words = line.split(' ')
        words=re.split(' |-',line)
    	word_list.extend(words) 
    return word_list  

#读取多个文件
def read_files(file_paths):
	final_words=[]
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#格式化一个单词		
def format_word(word):
    fmt = 'ABCDEFGHIJKLMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz-'#如果不加大写字母很多单词不就没首字母了吗
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

#格式化多个单词
def format_words(words):
	word_list=[]
	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

#用字典统计单词出现次数
def statistics_words(words):
	s_words={}
	for word in words:
		if s_words.has_key(word):
			s_words[word]=s_words[word]+1
		else:
			s_words[word]=1
	return s_words

#输出csv文件
def print_to_csv(volcaulay_map,to_file_path): 
    nfile=open(to_file_path,'w+') 
    for key in volcaulay_map.keys(): 
        nfile.write("%s,%s\n"%(key,volcaulay_map[key])) 
    nfile.close()

#把多个文件路径做成一个列表方便一起读取
def get_file_from_folder(folder_path):
    file_paths=[]
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


def main():
    #读取文本
	words=read_files(get_file_from_folder('data2'))
	print'获得未格式化的单词%d个 '%(len(words))
    #清洗单词
	f_words=format_words(words)
	print '获取已格式化的单词%d个 '%(len(f_words))
    #统计词频
	word_dict=statistics_words(f_words)
    #输出
	print_to_csv(word_dict,'output/test.csv')
if __name__ == "__main__":
    main()
