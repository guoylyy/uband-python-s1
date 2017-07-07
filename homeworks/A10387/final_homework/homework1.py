# -*- coding: utf-8 -*-
# author: kudari

# 1. 先用 data1/dt01.txt 的文档数据，大概200个单词，实现单词读取的类 WordReader
#    这个类的功能有几个
#    1）从一个路径里读取txt文件
#    2）把txt的文件分割成一个个单词
#    3) 对单词进行统计计数
#    4）排序
#    3）输出csv

import codecs
import os
import os.path
from operator import itemgetter, attrgetter
from collections import Counter

# 1.读取文件夹中所有文件
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

def readAllFile(folderpath, word_list):
	for root, dirs, files in os.walk(folderpath):
		for file in files:
			filepath = os.path.join(root, file)
			word_list = readFile(filepath, word_list)
	return word_list


# 2.读取一份文件
def readFile(filepath, word_list):
	f = open(filepath)
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		words = line.split(" ") # 用空格分割
		words = word_split(words) # 用-分割
		word_list += words
	return word_list

# 2.格式化文件
def formatFile(word_list):
	standardList = []
	fmt = 'abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for index, string in enumerate(word_list):
		for char in string:
			if char not in fmt:
				string = string.replace(char, '')
		if string != '':
			standardList.append(string.lower())
	return standardList

# 3.1 计数
def count(myList):
	myDic = Counter(myList)
	# mySet = set(myList)
	# for item in mySet:
	# 	myDic[item] = myList.count(item)
	return myDic

# 3.2 排序
def sort(dic):
	return sorted(dic.items(), key = itemgetter(1), reverse = True)

# 4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    # nfile.write("%s,%s\n" % ("words","counts")) 
    for index in range(len(volcaulay_map)):
        voc = volcaulay_map[index][0]
        times = volcaulay_map[index][1]
        nfile.write("%s,%s\n" % (str(voc), times))
    nfile.close()
    
def main():
	iniList = []
	# words = readFile("data1/dt01.txt",iniList)
	# print "获取了未格式化的单词 %d 个" % len(words)
	# myList = formatFile(words)
	# print "获取了格式化的单词 %d 个" % len(myList)
	# myDic = count(myList)
	# myVocMap = sort(myDic)
	# print_to_csv(myVocMap, "/Users/kudari/workspaces/final_homework/output/result-dt01.txt")

	words = readAllFile("/Users/kudari/workspaces/final_homework/data2", iniList)
	print "获取了未格式化的单词 %d 个" % len(words)
	myList = formatFile(words)
	print "获取了格式化的单词 %d 个" % len(myList)
	myDic = count(myList)
	print "计数完毕"
	myVocMap = sort(myDic)
	print "排序结束"
	print_to_csv(myVocMap, "/Users/kudari/workspaces/final_homework/output/test.csv")
	print "计算结束"

if __name__ == "__main__":
    main()
