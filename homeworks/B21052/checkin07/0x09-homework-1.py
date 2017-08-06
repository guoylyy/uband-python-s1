#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def homework1():
	dictionary = {'caramel':'firm chewy candy made from caramelized sugar and butter and milk',
				  'is':'the third person singular of the present tense of be ',
				  'handsome':'very beautiful'
				  }
	print len(dictionary) #长度

	#获取keys
	print dictionary.keys() #获得keys的列表,所有单词

	#获得values
	print dictionary.values() #获得values的列表，所有解释

	#是不是在
	print dictionary.has_key('caramel') #有，输出结果为True
	print dictionary.has_key('bad')  #灭有，输出结果为False

	#增加
	dictionary['bad'] = 'not very good'
	print dictionary
	print len(dictionary)

	#修改modify
	dictionary ['bad'] = 'failing to reach an acceptable standard'

	#删除delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)

	#for循环
	print '------------------'
	print dictionary['caramel']
	if dictionary.has_key('bad'):
		print dictionary['bad']   #这一段不执行
	else:
		print '没有bad这个单词'
	print '-------------------'

	#for遍历列表
	for key in dictionary.keys():
		print key    #单个单词
		print dictionary[key]   #相对应的解释

if __name__ == '__main__':
  homework1()