# -*- coding: utf-8 -*-
import os
import codecs

def get_file_from_folder(folder_path):
	for root,dirs,files in os.walk(folder_path):
		for file in files:
			file_path=os.path.join(root,file)
			print file_path
			
	return file_path
	
def read_file(file_path):
	f=codecs.open(file_path,'r','utf-8')
	lines=f.readlines()
	word_list=[]
	for line in lines:
		line=line.strip()
		words=line.split()
		word_list.extend(words)
	return word_list
def format_word(word):
	fm='abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fm:
			word=word.replace(char,'')
	return word.lower()
def format_words(words):
	word_list=[]
	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
			word_list.sort()
	return word_list
	
def sort_words(words):
	#word_list=format_words(words)
	#lst=word_list.sort()
	#return lst
	pass
def count_words(words):
	lst=format_words(words)
	number=[]
	dictionary={}
	for word in words:
		nm=lst.count(word)
		number.append(nm)
		d=dict(zip(lst,number))
	return d
def print_to_csv(d,to_file_path):
	nfile=open(to_file_path,'w+')
	for key in d.keys():
			val=d[key]
			nfile.write("%s,%s\n"%(key,str(val)))
	nfile.close()


def main():
	path=get_file_from_folder('data2')
	words=read_file(path)
	print words
	print '未格式化的单词有%d个'%(len(words))
	f_words=format_words(words)
	print f_words
	print '已格式化的单词有%d个'%(len(f_words))
	c_words=count_words(words)
	print c_words
	print_to_csv(c_words,'output/homework.csv')


if __name__ == "__main__":
    main()
