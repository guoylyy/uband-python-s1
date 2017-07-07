#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
# Filename day9 homework1
def main():
	dictionary = {
				  'good':'of a favorable character or tennency',
				  'none':'not any such thing or person',
				  'nice':'very beautiful'
	}
	print len(dictionary) #长度
	#获得键值
	print dictionary.keys() #key值的列表
	#获得value
	print dictionary.values()
	#是不是在
	print dictionary.has_key('good')
	print dictionary.has_key('bad')
	#Add
	dictionary['bad'] = 'not very good'
	#Modify
	dictionary['bad'] = 'falling to reach an acceptable standard'
	print dictionary
	#delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)
	#Get value
	print '---------------'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有 bad 这个单词'
	print '---------------'

	# iterator
	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
	main()