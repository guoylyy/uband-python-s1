# -*- coding: utf-8 -*-

# 读取文件~~~~~~~~

import codecs
import os

#批量读取
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words
def get_file_from_folder(folder_path):
	file_paths = []
	for root,dirs,files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root,file)
			file_paths.append(file_path)
	return file_paths

#1.读取文本
def read_file(file_path): 
    f = codecs.open(file_path, 'r', "utf-8") 
    lines = f.readlines() 
    word_list=[] 
    for line in lines: 
        line = line.strip() 
        words = line.split(' ') 
        words = word_split(words) #将words传到word_split，接受返回的值
        word_list.extend(words) 
    return word_list 
#readlines一次读取整个文件,自动将文件内容分析成一个行的列表
#2.清洗文本
#第一步单词过滤清洗,把不是下面字母的单词过滤掉
def format_word(word):
    fmt='abcdefghijkmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word=word.replace(char,'')
    return word.lower()
#字符串中所有大写字符为小写

#第二次单词过滤
def format_words(words):
    word_list=[] 
    for word in words:
        wd=format_word(word)
        if wd:
            word_list.append(wd)
    return word_list

#第三次单词过滤
def word_split(words): #接受从read_file传过来的words 
    new_list=[]
    for word in words:
        if '-' not in word: # 如果 - 不在words执行
            new_list.append(word) #添加word到new_list
        else:
            lst=word.split('-') #在的话split函数按 - 分割单词
            new_list.extend(lst) #extend函数用旧列表lst替换新列表 new_list
    return new_list #返回结果 new_list

#3.统计单词和排序
def statictcs_words(words):
    s_word_dict={}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word]=s_word_dict[word]+1
        else:
            s_word_dict[word]=1
    return s_word_dict
#4.输出文件
def print_to_csv(volcaulay_map,to_file_path):
    nfile=open(to_file_path,'w+')   
    for key in volcaulay_map.keys():  
        values=volcaulay_map[key]
        nfile.write("%s,%s\n"%(key,values))                                          
    nfile.close()

 #总函数
def main():
    #words=read_file('data/2016.01.02.txt') 
    paths = get_file_from_folder('data2')
    words = read_files(paths)
    f_words=format_words(words)
    word_dict=statictcs_words(f_words)
 
    print_to_csv(word_dict,'output/test4.csv')

if __name__ == '__main__':
	main()