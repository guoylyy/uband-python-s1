#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	dictionary = {
	# 'key': 'value'
	'good': 'of a favorable character or tendenc',
	'none': 'not any such thing or person',
	'nice': 'very beautiful'
	}
	#字典长度
	print len(dictionary)

	#获得keys
	print dictionary.keys()

	#获得value
	print dictionary.values()

	#字典是否存在key  如果键在字典dict里返回true，否则返回false
	print dictionary.has_key('good') #是 True
	print dictionary.has_key('bad')#否False

	#add key
	dictionary['bad'] = 'not very good' #为什么出现在nice前面
	print dictionary

	#modify key
	dictionary['bad'] = 'failing to reach an acceptable standard'
	print dictionary

	#delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)

	#get value
	print '---------'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有 bad 这个单词'
	print '---------'

	#iteator
	for key in dictionary.keys():
		print key
	#访问字典里的值[]
		print dictionary[key]

if __name__ == '__main__':
	main()