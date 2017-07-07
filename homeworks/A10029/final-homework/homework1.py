# -*- coding: utf-8 -*-
# @author: zi le

#基本思路：读取文件，分词，存入字典，key为单词，value为词频

import os,string,codecs
import re,csv

#读取文件并转化为列表
def read_file(file_path):
	f=open(file_path,'r')#打开文件
	read=f.read()#读取整个文件
	file=re.sub('[^a-zA-Z]',' ',read)#替换除字母以外的字符为空格
	words=re.split(' ',file)#以空格分割字符串
	words_list=words_clean(words)#去除空元素
	f.close()
	return words_list

def words_clean(words):#清洗空白元素
	words_list=[]
	for word in words:
		if word:
			words_list.append(word)

	return words_list


#读取多个文件
def read_files(file_paths):
	words=[]
	for path in file_paths:
		words.extend(read_file(path))
	return words


#通过字典进行单词计数
def word_count(words):
	dic={}#定义一个空字典
	for word in words:#遍历列表words里的所有元素
		word=word.lower()#字母全改为小写
		if dic.has_key(word):#判断字典里是否有相应元素key
			dic[word]=dic[word]+1#如有则元素key所对应value+1
		else:
			dic[word]=1#如没有则元素key所对应value为1
	lst=sorted(dic.items(),key=lambda item:item[1],reverse=True)#转化为按词频既value从大到小排序的列表数据
	
	return lst

#读取文件夹中的所有文件
def get_file_from_folder(folder_path):
	file_paths=[]
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths
#统计结果输出成csv文件
def output_csv(volcaulary_list,output_path):
	
	output_file = csv.writer(file(output_path, 'wb'))
	output_file.writerow(['单词 ', '次数 '])
	# print volcaulary_list
	for words in volcaulary_list:
		output_file.writerow(words)


def main():
	#文件路径
	in_path='data2'
	out_path='output/text1.csv'
	#读取文件并分割返回list数据
	# word=read_file(in_path)
	paths=get_file_from_folder(in_path)
	word=read_files(paths)
	print '获取单词数量 %s '%(len(word))
	#单词计数排序
	lst=word_count(word)
	print '获取归类后单词数量 %s '%(len(lst))
	#统计结果输出
	output_csv(lst,out_path)



if __name__ == "__main__":
    main()
