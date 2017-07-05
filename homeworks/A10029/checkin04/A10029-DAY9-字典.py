#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

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
	dictionary={'good':'of a favorable character or tendenc','none':'not any such thing or person','nice':'very beautiful'}
	#字典长度
	print len(dictionary)
	#获得字典keys
	print dictionary.keys()
	#获得字典value
	print dictionary.values()
	#判断字典里是否有
	print dictionary.has_key('good')
	print dictionary.has_key('bad')
	#给字典添加key
	dictionary['bad']='not very good'
	print dictionary
	#更新字典
	dictionary['bad']='failing to reach an acceptable standard'
	print dictionary
	#删除key
	del dictionary['bad']
	print dictionary
	print len(dictionary)
	#取值
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '字典里没有bad这个单词 '
	#遍历
	for key in dictionary.keys():
		print key
		print dictionary[key]

	print'-----------------------------------------'	

def homework2():
	dictionary={'abandon':'to give up to the control or influence of another person or agent',
							'abase':'to lower in rank, office, prestige, or esteem',
							'abash':'to destroy the self-possession or self-confidence of'}
	print '老爸正在用字典查英语单词 '
	if dictionary.has_key('etiquette'):
		print '老爸查了单词etiquette，得到了解释%s '%(dictionary['etiquette'])
	else:
		print '老爸查了单词etiquette，没有查到 '	
		print '老爸很生气，撕掉了含有单词abandon的这一页 '
		del dictionary['abandon']
	print dictionary	

	if dictionary.has_key('abase'):
		print '老爸查了单词abase，得到了解释%s'%(dictionary['abase'])
		print '老爸很开心，把abandon加入了词典 '
		dictionary['abandon']='to give up to the control or influence of another person or agent'
	else:
		pass	
	print dictionary	




if __name__ == '__main__':
  homework1(),homework2()