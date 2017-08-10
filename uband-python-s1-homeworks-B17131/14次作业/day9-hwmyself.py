#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt

#字典：eg. abandon "to give up to the control or influence of another person or agent"
#两个要素: Key    =>    value 
#字典有什么用：存储，查询
#1.花括号。一组Key.一组value 其中Key是不能重复的。每一个Key value是用冒号':'来分割的，每一组key value是用逗号','来分割的**

#初级练习（实战）(跟着老师打一遍)

def main():
	dictionary={'good':'of a favorable character or tendency',
				'none':'not any such thing or person',
				'nice':'very beautiful'}
	#长度 
	print len(dictionary)

	#获得keys
	print dictionary.keys() #获得key的列表

	#获得value
	print dictionary.values() #获得values的列表

	#是不是在(如何判断有没有这个key)
	print dictionary.has_key('good') #有-True
	print dictionary.has_key('bad') #没有-False

	#add
	dictionary['bad']= "not very good"
	print dictionary
	print len(dictionary)

	#modify(对dictionary某一个Key的解释进行修改)
	dictionary['bad']="failing to reach an acceptable standard"
	print dictionary

	#delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)

	#get value
	print '-------'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad'] #这一段没执行
	else:
		print '没有bad这个单词'

	#iterator 遍历	
	for key in dictionary.keys():
		print key #获得Key
		print dictionary[key] #获得value

if __name__ == '__main__':
	main()

