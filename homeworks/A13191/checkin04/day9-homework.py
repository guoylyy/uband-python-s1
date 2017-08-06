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

def homework2():
	dict2={
	'abandon':"to give up to the control or influence of another person or agent",
	'abase':"to lower in rank, office, prestige, or esteem",
	'abash':"to destroy the self-possession or self-confidence of"
	}

	if dict2.has_key('etiquette'):
		print dict2['etiquette']
	else:
		print "error"
	del dict2['abandon']
	print dict2['abase']
	dict2['abandon']='to give up to the control or influence of another person or agent'

def homework1():
	dict1={
	'good':"of a favorable character or tendency",
	'none':"not any such thing or person",
	'nice':"very beautiful"
	}

	print len(dict1)
	print dict1.keys()
	print dict1.values()

	print dict1.has_key('good')
	print dict1.has_key('bad')

	dict1['bad']='not very good'
	dict1['bad']='failing to reach an acceptable standard'
	print dict1

	del dict1['bad']
	print dict1
	print len(dict1)

	print '----'
	print dict1['good']
	if dict1.has_key('bad'):
		print dict1['bad']
	else:
		print "There is no 'bad' in the dictionary."
	print '----'

	for key in dict1.keys():
		print key
		print dict1[key]

if __name__ == '__main__':
  homework1()
  homework2()