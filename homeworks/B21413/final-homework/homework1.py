# -*- coding: utf-8 -*-

import codecs
import os

#1.读取文件.获取文档
def read_file(file_path): #read_file函数，file_path为需要读取的文件
	f = codecs.open(file_path,'r','utf-8')  #将打开文件的命令函数赋值给f
											#内部分别为file_path要打开的文件,r为打开方法：只读,utf为编码
	lines = f.readlines() #readlines用于读取 所有行，被赋值给 lines
	word_list = []
	for line in lines:
		line = line.strip() #python自带的函数strip()用以去掉指定字符串额字符
		words = line.split(" ") #对分割字符串进行切片,用空格分割
		words = word_split(words) #用-分割
		word_list.extend(words) #将words加入列表以统计

	return word_list

def read_files(file_paths):          #读取多个files
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words

#1.1 再分割一次
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)

	return new_list

#2.获取格式化之后的单词,清洗文本
def format_word(word):
	fmt = 'abcdefghijklmnopqrstuvwxyz-' #设置我们所需的字符串

	for char in word: #遍历
		if char not in fmt: #判断字符有没有fmt存在的字母，如果没有则替换
			word = word.replace(char,'') #replace是替换旧字符，这里的意思是用空格替换char

	return word.lower()

def format_words(words): #format 一群单词
	word_list = []
	for word in words:
		word_list.append(format_word(word))

	return word_list

#3.统计单词数目
def statictcs_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	return s_word_dict


#4.读取文件夹里的所有文件
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths

#5.输出成csv
def print_to_csv(volcaulay_map, to_file_path):#管理的过程使用字典&地址
    nfile = open(to_file_path,'w+') #赋值nfile以 to_file_path和写入方式‘w+''
    for key in volcaulay_map.keys(): #遍历字典的所有keys
        val = volcaulay_map[key] #values为数字
        nfile.write("%s,%s\n" % (key, str(val))) #写入,#\n 换行
    nfile.close()

def main():
    #1. read file
    words = read_files(get_file_from_folder('data2'))
    	#words = read_files['data2....']
    print '获取了未格式化的单词 %d 个'% (len(words))
    #2. format word
    f_words = format_words(words)
    print '获取了已经格式化的单词 %d 个'% (len(words))
    #3. statictcs
    word_dict = statictcs_words(f_words)
    del word_dict['']
    #4. 输出成csv
    print_to_csv(word_dict, 'output/test.csv')



    

if __name__ == "__main__":
    main()
