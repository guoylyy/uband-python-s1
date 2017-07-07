#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu

#作业1:对照 day9 sample-code 打一遍代码

def main():
	dictionary = {
	              'good':'of a favorable character or tendenc',
	              'none':'not any such thing or person',
	              'nice':'very beautiful'
	             }

	#输出字典的长度            
	print len(dictionary)
	#获取字典中所有的内容
	print dictionary
	#获取字典中所有的keys
	print dictionary.keys()
	#获取字典中所有的values
	print dictionary.values()
	#判断某一个key是否在dictionary中,输出值为True（1） 或者 False（0），
	print dictionary.has_key('good')
	print dictionary.has_key('bad')
	if dictionary.has_key('good'):
		print dictionary['good']
	else:
		print '字典中不存在 good '
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '字典中不存在 bad '
	#在字典中增加一个key-value
	dictionary['bad'] = 'not very good'
	print dictionary
	#修改字典中某一个key对应的value
	dictionary['bad'] = 'failing to reach an acceptable standard'
	print dictionary
	#删除字典中的某个key-value
	del dictionary['good']
	print dictionary  
	#取字典中某一个key对应的value
	print dictionary['none']
	#分别输出字典中所有的keys或者values
	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
  main()