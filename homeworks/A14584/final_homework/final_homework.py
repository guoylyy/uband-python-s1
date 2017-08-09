#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最后一次大作业
# @author: Chuan

import codecs
import os

#从文件中读取文本
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    para=[]
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        para.extend(words)
    return para

#一次读取多个文件
def read_files(file_paths):
	final_para=[]
	for path in file_paths:
		final_para.extend(read_file(path))
	return final_para

#处理单词，保留数字和本身就带有连接字符“-”的单词
def format_word(word):
	fmt='abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	for char in word:
		if char not in fmt:
			word=word.replace(char,'') 
	return word.lower()  

#处理单词序列
def format_words(words):
	word_list=[] 

    for word in words: 
        wd=format_word(word)
                            
        if word!='':
            word_list.append(wd) 
    return word_list


#获取路径
def get_file_from_folder(folder_path):
	file_paths=[]
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path=os.path.join(root,file)
			file_paths.append(file_path)

	return file_paths

#统计词频
def frequency_word(words):
	word_dict={}
	for word in words:
		if word_dict.has_key(word):
			word_dict[word]=word_dict[word]+1
		else:
			word_dict[word]=1

	return word_dict

#处理单词，去掉以上处理后剩下的空格和长串网址信息
def dict_modify(word_dict):
	new_dict={}
	for key in word_dict.keys():
		if (key=='') or ('httpwwwecnomistcom'in key):
			pass
		else:
			new_dict[key]=word_dict[key]

	return new_dict

#排序与拆分
def sort_dict(word_dict):
	final_lst=sorted(word_dict.items(), key=lambda item:item[1], reverse=True)
	word=[]
	frequency=[]
	for i in range(len(final_lst)):
		word.append(final_lst[i][0])
		frequency.append(final_lst[i][1])

	return (word, frequency)

#导出CSV表格
def print_to _csv(final_tup, to_file_path):
	nfile=open(to_file_path,'w+')
	for i in range(len(final_tup[0])):
		nfile.write('%s,%s\n'%(final_tup[0][i],final_tup[1][i]))

	nfile.close()

def main():
	words=read_files(get_file_from_folder('data2')) #读取文件
	print "%d unformatted words got."%(len(words))
	f_words=format_words(words) #处理单词
	print "%d formatted words got."%(len(f_words)) 
	m_dict=dict_modify(frequency_word(f_words)) #再次处理单词
	print_to_csv(sort_dict(m_dict), 'output/test1.csv')


if __name__ == '__main__':
	main()
