#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业1:对照 day9 sample-code 打一遍代码
#
#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又差了一个单词 'abase' 得到了解释
# 老爸很开心，有把 'abandon' 加入到了字典里
# 
def homework1():
	dictionary = {'baba':'60', 'mama':'54', 'sister':'30', 'me':'23'}

	print len(dictionary)
	print dictionary.keys()
	print dictionary.values()
	print dictionary.has_key('nainai')
	print dictionary.has_key('me')
	dictionary['haohao'] = '3'
	print dictionary
	dictionary['nainai'] = '70'
	print dictionary
	dictionary['haohao'] = '4'
	print dictionary
	del dictionary['haohao']

	print dictionary['me']
	if dictionary.has_key('mama'):
		print dictionary['mama']

	for key in dictionary.keys():
		print "%s = %s" %(key, dictionary[key])


def homework2():
	dictionary = {'abandon':'to give up to the control or influence of another person or agent', 'abash':'to destroy the self-possession or self-confidence of', 'abase':'to lower in rank, office, prestige, or esteem '}
	if dictionary.has_key('etigue'):
		print dictionary['etique']
	else:
		print "没有这个词"
	del dictionary['abandon']
	print dictionary['abase']
	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print len(dictionary)
if __name__ == '__main__':
  homework1()
  homework2()