#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi


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

  print '老爸在看一本英文书,他旁边有一个词典,但是只有三个词的解释 '
  print '它们分别是：'

  #遍历
  dictionary = {
				'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem',
				'abash':'to destroy the self-possession or self-confidence of'
				}
  for key in dictionary.keys():
    print key
    print dictionary[key]

  #取值
  print '老爸先查了一个单词"etiquette"'
  if dictionary.has_key('etiquette'):
  	print dictionary['etiquette']
  else:
  	print '没有查到好尴尬哦~'

  #删除
  del dictionary['abandon']
  print '老爸怒了,把"abandon"单词那一页撕掉了'
  print '字典变成了'
  print dictionary

  #取值
  print '老爸又查了单词"abse"'
  print '它的解释是'
  print dictionary['abase']
  if dictionary.has_key('abase'):
  	print '单词查到了,老爸好开心'

  #add
  dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
  print '老爸一高兴,又把"abandon"那一页贴回去了'
  print dictionary


if __name__ == '__main__':
	homework2()