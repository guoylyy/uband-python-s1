#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

def homework1():
  print '已经截图提交'
  print '------'

def homework2():
  print '老爸在看一本英文书，他旁边有一个词典，但是只有三个单词的解释'

  dictionary = {'abandon':'to give up to the control or influence of another person or agent',
  'abase':'to lower in rank, office, prestige, or esteem',
  'abash':'to destroy the self-possession or self-confidence of '}

  print '老爸先查了一个单词'
  if dictionary.has_key('etiquette'):
	print dictionary['etiquette']
  else:
	print '没有查到，老爸怒了'
  
  del dictionary['abandon']
  print '把含有 abondon 一页的单词撕掉了'

  print '然后老爸又查了一个单词 abase'
  if dictionary.has_key('abase'):
	print dictionary['abase']
  else:
	print '得到了解释，老爸很开心'

  dictionary['abandon'] = "to give up to the control or influence of another person or agent"
  print '又把 abandon 加入到了字典里'
  print len(dictionary)
  print dictionary.keys()
  print dictionary.values()

if __name__ == '__main__':
  homework1()
  homework2()