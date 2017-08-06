#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi

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
  				'none':'not any such thing or person',
  				'nice':'very beautiful'
  				}
  #长度				
  print len(dictionary)

  #获得keys列表
  print dictionary.keys()

  #获得values列表
  print dictionary.values()

  #是不是在字典中
  print dictionary.has_key('none')
  print dictionary.has_key('bad')

  #add
  dictionary['bad'] = 'not very good'

  #modify
  dictionary['bad'] = 'falling to reach an acceptable standard'
  print dictionary
  
  #delete
  del dictionary['bad']
  print dictionary
  print len(dictionary)

  #get value
  print dictionary['good']
  if dictionary.has_key('bad'):
  	print dictionary['bad']
  else:
  	print '没有 bad 这个词'

  #iterator
  for key in dictionary.keys():
  	print key
  	print dictionary[key]





if __name__ == '__main__':
  homework1()