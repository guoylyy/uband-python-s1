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
	dictionary	=	{'good':'of a favorable character or tendenc',
					 'none':'not any such thinf or person',
					 'nice':'very beautiful'
					 }	

	print	len(dictionary)
	#获得key
	print	dictionary.keys()
	#获得value
	print	dictionary.values()
	#是不是在
	print	dictionary.has_key('good')
	print	dictionary.has_key('good2')
	#add
	dictionary['bad']	=	"inadequate or unsuited to a purpose"
	print	dictionary
	print	len(dictionary)

	print	'------'
	#modify
	dictionary['bad']	=	'joke'
	print	dictionary
	print	len(dictionary)
	#delete
	del	dictionary['bad']
	print	dictionary
	print	len(dictionary)
	#if
	if dictionary.has_key('bad'):
		print	dictionary['bad']
	else:
		print	'没有这个值'
	#for  
	for key in dictionary.keys():
		print	key
		print	dictionary[key]
def homework2():
	dictionary	=	{'abandon':'to give up to the control or influence of another person or agent',
					 'abase':'to lower in rank,office,prestige,or esteem',
					 'abash':'to destory the self-possession or self-confidence of'
					 }
	print	"老爸先查了一个单词'etiquette'，没有查到"
	if dictionary.has_key('etiquette'):
		pass
	else:
		print	"老爸怒了，把含有'abandon'一页的单词撕掉了"
		del	dictionary['abandon']
		print	dictionary
		print	len(dictionary)

	print	"老爸又查了一个单词'abase'得到了解释"
	if dictionary.has_key('abase'):
		print	"老爸很开心，又把'abandon'加入了字典里"
		dictionary['abandon']	=	'to give up to the control or influence of another person or agent'
		print	dictionary
		print	len(dictionary)
	else:
		pass

if __name__ == '__main__':
  homework1()
  print	'----------------'
  homework2()