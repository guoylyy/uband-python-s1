#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Emma


def homework1():
	dictionary = {
					'good':'of a favorable character or tendenc',
					'none':'not any such thing or person',
					'nice':'very beautiful'
					}

	print len(dictionary) #长度

	print dictionary.keys() #获得keys的列表

	print dictionary.values() #获得values的列表


	#查询这个字典中是否有想要找到的key
	print dictionary.has_key('good') #字典中有这个key
	print dictionary.has_key('bad') #字典中没有这个key

	
	#add
	print '============='
	dictionary['bad'] = 'not very good'
	print dictionary
	print len(dictionary)


	#modify
	dictionary['bad'] = 'failing to reach an acceptable standard'
	print dictionary


	#delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)


	#get value 取值
	print '============='
	print dictionary['good']
	if dictionary.has_key('bad'):
		print ditionary['bad']
	else:
		print '没有 bad 这个单词'
	print '======================'

	#iterator 遍历
	for key in dictionary.keys():
		print key
		print dictionary[key]


def homework2():
	print '======================'
	print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释'
	dictionary = {'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem',
				'abash':'to destroy the self-possession or self-confidence of'
				}
	if dictionary.has_key('etiquette'):
		print ditionary['etiquette']
	else:
		print '老爸查了单词"etiquette"没有查到,老爸怒了,把含有"abandon"一页的单词撕掉了'
	if dictionary.has_key('abase'):
		print '然后老爸又查了一个单词"abase",得到了解释'
		print dictionary['abase']
		print '老爸很开心，又把"abandon"加入到了字典里'
	else:
		print '23333333'


if __name__ == '__main__':
	homework1()
	homework2()