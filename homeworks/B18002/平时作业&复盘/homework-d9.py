#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

def homework1():
	dictionary = {
								'good':'of a favorable chracter or tendency',
								'none':'not any such thing or person',
								'nice':'very beautiful'
								}

	# length of the dictionary
	print len(dictionary)

	# keys
	print dictionary.keys()

	# values
	print dictionary.values()

	# true or false
	print dictionary.has_key('nice')
	print dictionary.has_key('YEAH')

	# add 
	dictionary['bad'] = 'not very good'
	print len(dictionary)

	# modify
	dictionary['bad'] = "failing to reach an acceptable standard"
	print dictionary

	# delete
	del dictionary['bad']
	print len(dictionary)

	# get value
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print 'The word "bad" cannot be found.'

	#	iterator
	print '~~~~~~~~~'
	for key in dictionary.keys():
		print key              # key
		print dictionary[key]  # value

def homework2():
	print '----------------------'
	print 'Homework 2'
	print 'Dad is reading an English book.'	
	dictionary = {
					      'abandon':'to give up to the control or influence of another person or agent',
								'abase':'to lower in rank, office, prestige, or esteem',
								'abash':'to destroy the self-possession or self-confidence of'
								}

	# 老爸查词		
	print 'Dad looks up "etiquette" in the dictionary.'
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']
	else:
		print 'Failing to find the word, he is so angry that he tears the page of "abandon". '
	
	# 老爸生气啦~~！
	del dictionary['abandon']
	print len(dictionary)

	# 老爸又查词
	print 'Dad looks up another word "abase" in the dictionary.'
	if dictionary.has_key('abase'):
		print 'The word "abase" means:',
		print dictionary['abase']
		print 'He is happy that he add "abandon" to the dictionary.'
	else:
		print 'He fails again.'

	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print len(dictionary)


if __name__ == '__main__':
	homework1()
	homework2()