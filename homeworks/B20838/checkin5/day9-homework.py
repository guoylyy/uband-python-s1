#!/usr/bin/python
# -*- coding: utf-8 -*-
#@author:lightningLUO

def homework2():
	print '老爸在看一本英文书，他旁边有一个字典'
	dictionary = {
					'abandon': 'to give up to the control or influence of another person or agent',
					'abase': 'to lower in rank, office, prestige, or esteem ',
					'abash': 'to destroy the self-possession or self-confidence of'
				}

	print '老爸先查了一个单词etiquette'
	
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']
	else:
		print '没有查到'
	
	print '老爸怒了，把含有abandon一页的单词撕掉了'
	del dictionary['abandon']

	print '然后老爸又查了一个单词abase'
	if dictionary.has_key('abase'):
		print dictionary['abase']
		print '查到了，老爸很开心,又把abandon加入到了字典里'
	else:
		'没有查到'

	dictionary['abadon'] = 'to give up to the control or influence of another person or agent'

	print dictionary
	print '-----------------------------------------------------------------------'

def homework1():
	dictionary = {
				'good': 'of a favorable character or tendence',
				'none': 'not any such thing or person',
				'nice': 'very beautiful'
				 }

	print len(dictionary)#长度
	print dictionary.keys()#获取Key的列表
	print dictionary.values()#获取values的列表

	print '-------'
	#判断是不是在
	print dictionary.has_key('good')#有
	print dictionary.has_key('bad')#没有

	#添加
	dictionary['bad'] = 'not very good'

	#修改
	dictionary['good'] = 'failing to reach an acceptable standard'
	print dictionary

	#删除
	del dictionary['bad']
	print dictionary
	print len(dictionary)

	#get value
	print '-------------'
	print dictionary['good']
	print '-------------'
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有bad这个单词'
	print '------------------'

	#iterator 迭代
	for key in dictionary.keys():
		print key
		print dictionary[key]






if __name__ == '__main__':
	homework2()
	homework1()