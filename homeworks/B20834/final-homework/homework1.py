#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import collections

def read_word(path): 
	file_open = open(path,'r')
	file_content = file_open.read().decode('utf-8')
	file_word = file_content.split(" ") #分行
   	fmt = 'abcdefghijklmnopqrstuvwxyz-'
   	for i in range(len(file_word)):
   		for char in file_word[i]:
   			if char not in fmt:
   				file_word[i] = file_word[i].lower().replace(char,'')
  	count = {}
   	for word in file_word:
   		if not count.has_key(word):
   			count[word] = 1
   		else:
   			count[word] = count[word] + 1
   	count = collections.OrderedDict(sorted(count.items(), key=lambda t: -t[1]))
   	return count
def print_to_csv(count, path):
	nfile = open(path,'w+')
	for key in count.keys():
		val = count[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()


def main():
    count = read_word('C:\Users\geniu\Documents\uband-python-s1\\final-homework\data1\dt01.txt')
    print_to_csv(count,'data1\dt02.txt')

if __name__ == "__main__":
    main()
