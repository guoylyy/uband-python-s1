#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业1:对照 day9 sample-code 打一遍代码
#
def homework1():
  dictionary = {
  				'good': 'of a favorable character or tendency',
  				'none': 'not any such thing or person',
  				'nice': 'very beautiful'
 			   }

  print len(dictionary) #长度
  #获得keys
  print dictionary.keys() #获取key的列表

  #获得value
  print dictionary.values() #获取values的列表

  #是不是在字典里
  print dictionary.has_key('good') #有
  print dictionary.has_key('bad') #没有

  #add
  dictionary['bad'] = 'not very good'

  #modify
  dictionary['bad'] = 'failing to reach an acceptable standard'
  print dictionary

  #delete
  del dictionary['bad']
  print dictionary
  print len(dictionary)

  #get value
  print '---'
  print dictionary['good']
  if dictionary.has_key('bad'):
  	print dictionary['bad'] #这一行没执行，因为之前delete了bad
  else:
  	print '没有 bad 这个单词'
  print '--- '

  #iterator
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
# 然后老爸又差了一个单词 'abase' 得到了解释
# 老爸很开心，有把 'abandon' 加入到了字典里
# 
def homework2():
  print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释:'
  dictionary = {
  				'abandon': 'to give up to the control or influence of another person or agent',
  				'abase': 'to lower in rank, office, prestige, or esteem',
  				'abash': 'to destroy the self-possession or self-confidence of'
 			   }
  for key in dictionary.keys():
  	print key, ':', dictionary[key]

  #老爸先查了一个单词 'etiquette' 没有查到
  print "老爸先查了一个单词etiquette"
  if dictionary.has_key('etiquette') == 1 :
  	print '老爸很开心。'
  else:
    print '没有查到，老爸怒了，把含有abandon一页的单词撕掉了。'

  del dictionary['abandon'] #把含有 'abandon' 一页的单词撕掉了
  print '字典里只剩',dictionary.keys()
  
  #然后老爸又查了一个单词 'abase' 得到了解释
  print '然后老爸又查了一个单词abase'
  if dictionary.has_key('abase'):
  	print '老爸很开心：'
  	print 'abase:', dictionary['abase'] 
  	print '又把abandon加入到了字典里。'
  else:
  	print '没有查到，老爸怒了。'

  #又把abandon加入到了字典里
  dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
  print '字典里现在有',dictionary.keys()



  	


if __name__ == '__main__':
  homework1()
  homework2()