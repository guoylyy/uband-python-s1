#!/user/bin/python
# -*- coding: utf-8 -*-
# 数一数文本中各个词汇出现的次数，输出词汇的出现频率
# 1. 先用 data1/dt01.txt 的文档数据，大概200个单词，实现单词读取的类 WordReader
#    这个类的功能有几个
#    1）从一个路径里读取txt文件
#    2）把txt的文件分割成一个个单词
#    3) 对单词进行统计计数
#    4）排序
#    3）输出csv
import csv
class WordReader:
	def __init__(self,filedir,writedir):
		self.filedir = filedir
		self.writedir = writedir
	# Read text from the file
	def read_file(self):
		file_object = open(self.filedir)
		try:
			all_text = file_object.read()
		finally:
			file_object.close()
		return all_text  #可以返回

	# Split the text into word
	def word_split(self,all_text):
		word_list = all_text.split(' ')
		
		word_low = []
		for w in word_list:
			word_low.append(w.lower())
		# print word_low
		return word_low

	# Calculate the number of every words
	# Saved in a dict type ---- key-word,value-count
	def word_count(self,word_list):
		word_dict = {}
		for word in word_list:
			if word_dict.has_key(word):
				word_dict[word] += 1
			else:
				word_dict[word] = 1
		# print type(word_dict)
		return word_dict

	# sort the words according to its count
	# the words were saved in a list --- key
	# the number of words were saved in a list ---value
	def word_sort(self,word_dict):
		key = word_dict.keys()
		key.sort()
		value = []
		for keys in key:
			value.append(word_dict[keys])
		return key,value

	# write the sorted list into a .csv file
	def write_csv(self,key,value):
		cvfile = file(self.writedir, 'w')
		writer = csv.writer(cvfile)
		length = len(key)
		# print len(value)
		writer.writerow(["Word","Count"])
		for item in range(0,length):
			writer.writerows([[key[item],value[item]]])
def redu(word_dict):
	new_wd ={}
    keys = word_dict.keys()
    for items in keys:
    	flag = True
    	items = items.strip(' ')
    	
    	for i in range(0,len(items)):
    		# 如何word中涉及数字或者$符号，则不进入word统计范围
    		if (items[i] >= '0' and items[i] <= '9') or items[i] == '$':
    			flag =False
    			break
    		else:
    			pass
    	# 去掉一些符号的影响
    	if flag :
    		items0 = items.strip()
    		items1 = items0.strip('\\')
    		items2 = items1.strip('(')
    		items3 = items2.strip(')')
    		items4 = items3.strip('"')
    		items5 = items4.strip(',')
    		items6 = items5.strip('.')
    		items7 = items6.strip('*')
    		items8 = items7.strip('\t')
    		items9 = items8.strip('"')
    		
    		if items9 == '':
    			pass
    		else:
    			new = items9
    			new_wd[new] = word_dict[items]
    return new_wd
def main():
	# homework #01
    filedir = 'data1/dt01.txt'
    writedir = 'output/test.csv'
    
    # Instance of class WordReader
    App = WordReader(filedir, writedir)
    all_text = App.read_file()
    # print all_text
    word_list = App.word_split(all_text)
    # print word_list
    word_dict = App.word_count(word_list)

    new_wd = redu(word_dict)	
    			
    # print new_wd
    key, value = App.word_sort(new_wd)
    # print word_sorted
    App.write_csv(key,value)


    # dict1 = {}
    # for i in range(1,6):
    # 	for j in range(2,7):
    # 		dict1[i] = j
    # print dict1
if __name__ == "__main__":
    main()
