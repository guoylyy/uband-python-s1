#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan
import codecs
import os
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt

class WordReader():
	def __init__(self,name):
		self.name = name

	#1）从一个路径里读取txt文件
	#2）把txt的文件分割成一个个单词
	def read_file(self,file_path): #要加self，否则报错takes exactly 1 argument (2 given)
		word_list = []
		f = codecs.open(file_path,'r','utf-8')
		lines = f.readlines()
		for line in lines:
			line = line.strip() #去掉头尾空格
			words = line.split(' ')
			word_list.extend(words)		
		return word_list #return要在最后

	#读取文件夹所有文件
	def get_file_from_folder(self,folder_path):
		path_list = []
		for root, dirs, files in os.walk(folder_path):
			for file in files:
				file_path = os.path.join(root, file)
				path_list.append(file_path)
		return path_list

	#格式化单词
	def format_word(self,word_list):
		words = []
		word_fmtlst = []
		fmt = 'abcdefghijklmnopqrstuvwxyz-'
		for word in word_list:
			word = word.lower()
			for char in word:
				if char not in fmt:
					word = word.replace(char,'')
			if word: #去掉空格
				words.append(word)
		for word in words:
			if '-' not in word:
				word_fmtlst.append(word)
			else:
				lst = word.split('-')
				word_fmtlst.extend(lst)
		return word_fmtlst

	#3) 对单词进行统计计数
	def count_word(self,word_fmtlst):
		vocabulary_map = {
		}
		for item in word_fmtlst:
			if vocabulary_map.has_key(item):
				vocabulary_map[item] = vocabulary_map[item] + 1
			else:
				vocabulary_map[item] = 1
		return vocabulary_map

	#排序（字典排序后变为list）
	def word_sort(self,vocabulary_map):
		sort_list = sorted(vocabulary_map.iteritems(), key=lambda d:d[1], reverse = True)
		return sort_list

	#输出csv
	def print_to_csv(self,sort_list, to_file_path):
		csvfile = open(to_file_path,'wb')
		for item in sort_list:
			val = item[1]
			csvfile.write("%s,%s\n" % (item[0], str(val)))
		csvfile.close()

	#画词云
	def darw_wordcloud(self,vocabulary_map,output_path):
		color_mask = imread('E:/python/final-homework/alice.png')
		wc = WordCloud(mask=color_mask,background_color='white',scale=1.5)
		my_wordcloud = wc.generate_from_frequencies(vocabulary_map)
		image_colors = ImageColorGenerator(color_mask)
		plt.imshow(my_wordcloud)
		plt.axis('off')
		plt.show()
		wc.to_file(output_path)




def main1():
	test = WordReader('test')
	
	word_list = test.read_file('data1/dt01.txt')
	print len(word_list)

	word_fmtlst = test.format_word(word_list)
	print len(word_fmtlst)

	vocabulary_map = test.count_word(word_fmtlst)
	
	sort_list = test.word_sort(vocabulary_map)

	test.print_to_csv(sort_list, 'E:/python/final-homework/output/test.csv')

	test.darw_wordcloud(vocabulary_map,'E:/python/final-homework/output/test.jpg')

def main2():

	txt = WordReader('txt')
	path_list = txt.get_file_from_folder('data2')
	word_list = []

	for file_path in path_list:
		lst = txt.read_file(file_path)
		word_list.extend(lst)
	print len(word_list)

	word_fmtlst = txt.format_word(word_list)
	print len(word_fmtlst)

	vocabulary_map = txt.count_word(word_fmtlst)

	sort_list = txt.word_sort(vocabulary_map)
	
	txt.print_to_csv(sort_list, 'E:/python/final-homework/output/123.csv')


if __name__ == "__main__":
	main1()
	main2()

#一开始计数的地方用了list.count，运算太复杂，试短的可以，长的跑了好几个小时，宛如一个智障hhhh