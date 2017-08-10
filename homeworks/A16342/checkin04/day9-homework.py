#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan
	
def hoemwork1():
	dictionary = {
	                'good':'of a favorable character or tendenc',
	                'none': 'not any such thing or person',
	                'nice': 'very beautiful'
		}


	#长度
	print len(dictionary)

	#keys
	print dictionary.keys()

	#values
	print dictionary.values()

	#是否在
	print dictionary.has_key('good')
	print dictionary.has_key('bad')

	#add
	dictionary['bad'] = 'not very good'

	#modify
	dictionary['bad'] = 'failing to reach an acceptable standard'

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
		print '没有bad这个词'
	print '----------'

	#iterator
	for key in dictionary.keys():
		print key
		print dictionary[key]
	print '----------------'
def homework2():
	print '老爸在看一本英文书'
	dictionary = {
				'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem',
				'abash':'to destroy the self-possession or self-confidence of'
	}

	print '老爸先查了一个单词 "etiquette"'
	if dictionary.has_key('etiquette'):
		print 'etiquette 的意思是 %s' % (dictionary['etiquette'])
	else:
		print '老爸没有查到etiquette的意思'
		del dictionary['abandon']
		print '老爸怒了，把含有 "abandon" 一页的单词撕掉了'

	print '-----------'
	print '老爸又查了一个单词"abase"'
	if dictionary.has_key('abase'):
		print 'abase 的意思是 %s' % (dictionary['abase'])
		dictionary['abadon'] = 'to give up to the control or influence of another person or agent'
		print '老爸很开心，又把 "abandon" 加入到了字典里'
	else:
		print '老爸没有查到abase的意思'

if __name__ == '__main__':
	hoemwork1()
	homework2()