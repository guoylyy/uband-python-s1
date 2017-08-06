#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: pluto

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
	dictionary = {
				'good':'of a favorable character or tendenc',
                'none': 'not any such thing or person',
                'nice': 'very beautiful'
                }
	print len(dictionary)#获取长度

	print dictionary.keys()#获取key的列表

	print dictionary.values()#获取value的列表

	print dictionary.has_key('lalal')#查询是否有某个词

	dictionary['bad'] = 'not very good'#添加一个词

	dictionary['bad'] = 'failing to reach an acceptable standard '#修改一个词
	print dictionary

	del dictionary['bad']#删除一个词

	print dictionary['good']#获取单个词的value

	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有这个单词'
		
	for key in dictionary.keys():#遍历
		print key
		print dictionary[key]

def homework2():
	pass

if __name__ == '__main__':
  homework1()