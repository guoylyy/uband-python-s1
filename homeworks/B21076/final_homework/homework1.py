# -*- coding: utf-8 -*-
import codecs
import os

class WordReader():

	#1.读取文件
	#读取文件夹里的所有文件
	def get_file_from_folder(self,folder_path):
		file_paths=[]
		for root, dirs, files in os.walk(folder_path):
			for file in files:
				file_path = os.path.join(root, file)
				file_paths.append(file_path)
				# print file_path
		return file_paths

	def read_files(self,file_path):
		final_words=[]
		for path in file_path:
			final_words.extend(self.read_file(path))
		return final_words
	#用-分割：aaa-bbb-ccc :: aaa, bbb,ccc
	def word_split(self,words):
		new_list=[]
		for word in words:
			if '-' not in word:
				new_list.append(word)
			else:
				lst=word.split('-')
				new_list.extend(lst)
		return new_list

	def read_file(self,file_path):
		f = codecs.open(file_path, 'r', "utf-8")
		lines = f.readlines()
		word_list=[]
		for line in lines:
			ine = line.strip()
			words = line.split(" ")
			words=self.word_split(words)
			word_list.extend(words)	
		return word_list

	#2.格式化后的单词
	def format_word(self,word): 
		fmt='abcdefghijkmnopqrstuvwxyz-' 
		for char in word: 
			if char not in fmt:
				word=word.replace(char,'') 
	
		return word.lower() 

	def format_words(self,words): 
		word_list=[]
		for word in words:
			wd=self.format_word(word) 
			if wd:
				word_list.append(wd)
		return word_list 

	#3.统计单词并排序
	def statistics_words(self,words):
		word_dict={}
		for word in words:
			if word_dict.has_key(word):
				word_dict[word]=word_dict[word]+1
			else:
				word_dict[word]=1
		# return word_dict
		return self.sort_words(word_dict)
	# 排序
	def sort_words(self,word_dict):
		
		dict= sorted(word_dict.iteritems(), key=lambda d:d[0]) 
		# print dict
		return dict

	#4.输出文件
	def print_to_csv(self,volcaulay_map,to_file_path):
		nfile = open(to_file_path,'w+')

		# for dkey in volcaulay_map.keys():
		# 	val = volcaulay_map[dkey]
		# 	nfile.write("%s,%s\n" % (dkey, str(val)))
		for item in volcaulay_map:
			nfile.write("%s,%s\n" % (item[0], item[1]))
		nfile.close()


   


def main():
	#1.读取文件
	# file_path='data/2016.01.02.txt'
	file_path='data2'
	wordReader=WordReader()
	# words=wordReader.read_file(file_path)
	words=wordReader.read_files(wordReader.get_file_from_folder(file_path))
	# print words 
	print'一共有%d个单词'%(len(words)) 
	#2.获取格式化后的单词
	f_words=wordReader.format_words(words)
	# print f_words
	print'一共格式化%d个单词'%(len(f_words)) 
	#3.统计单词并排序
	word_dict=wordReader.statistics_words(f_words)
	# print word_dict

	#4.输出文件
	file_path='output/test.csv'
	wordReader.print_to_csv(word_dict,file_path)

	
if __name__ == "__main__":
    main()
