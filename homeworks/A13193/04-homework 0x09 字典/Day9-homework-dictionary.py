#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania


#作业1:对照 day9 sample-code 打一遍代码

def homework1():
  dictionary = {
                'good':'of a favorable character or tendency',
                'none': 'not any such thing or person',
                'nice': 'very beautiful'
               }

  print len(dictionary)   #获得字典中的元素个数

  print dictionary.keys()  #获得keys的列表

  print dictionary.values()  #获得values的列表  

  print dictionary.has_key('good')  #keys中有“good”
  print dictionary.has_key('pensylvania')  #keys中没有“pennsylvania”

  #add在字典中添加key
  dictionary['pennsylvania'] = "name of a state in the United States"
  print dictionary
  print len(dictionary)
  #modify在字典中寻找正确的释义
  dictionary['pennsylvania'] = "a hybrid formed from the surname Penn + Latin sylvania."
  print dictionary
  #delete删除这一词条
  del dictionary['pennsylvania']
  print dictionary
  print len(dictionary)

  #取值: get value
  print '---'
  print dictionary['good']
  if dictionary.has_key('pennsylvania'):
  	print dictionary['pennsylvania']
  else:
  	print '没有 pennsylvania 这个单词'
  print '---'

  #遍历：iterator
  for key in dictionary.keys():
  	print key
  	print dictionary[key]


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
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里

def homework2():
  dictionary = {
                'abandon':'to give up to the control or influence of another person or agent',
                'abase': 'to lower in rank, office, prestige, or esteem',
                'abash': 'to destroy the self-possession or self-confidence of'
               }

  print '---------------------'
  #在字典中查etiquette
  if dictionary.has_key('etiquette'):
  	print dictionary['etiquette']
  else:
  	print '没有 etiquette 这个单词'
  print '---' 
  #怒！撕掉abandon
  del dictionary['abandon']
  print dictionary 
  print len(dictionary)
  #在字典中查abase
  print '---' 
  print dictionary.has_key('abase')
  if dictionary.has_key('abase'):
  	print dictionary['abase']
  else:
  	print '没有 abase 这个单词'
  print '---'
  #开心！加回abandon
  dictionary['abandon'] = "to give up to the control or influence of another person or agent"
  print dictionary
  print len(dictionary)      


if __name__ == '__main__':
  homework1()
  homework2()