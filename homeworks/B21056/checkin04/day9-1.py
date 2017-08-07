#!/usr/bin/python
#-*- coding:utf-8 -*-
#@author:xxx

def main():
	dictionary={
				'good':'of a favorable character or tendenc',
				'none':'not any such thing or person',
				'nice':'very beautiful'
				}

	print len(dictionary)#长度
	print dictionary.keys()#获得key
	print dictionary.values()#获取values的列表
	#查找在定义的字典中是否存在
	print dictionary.has_key('good')#有->返回True
	print dictionary.has_key('bad')#没有->返回False
	#add/modify
	dictionary['bad']='not very good'
	dictionary['bad']='failing to reach an acceptable standard'#覆盖
	print dictionary
	#delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)

	#get value
	print '---------------'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有bad这个词'
	print '---------------'

	#iterator
	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
	main()