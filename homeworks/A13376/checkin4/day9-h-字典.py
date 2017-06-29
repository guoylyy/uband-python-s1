#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yikuai

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
  				'good': 'of a favorable character or tendenc',
  				'none': 'not any such thing or person',
  				'nice': 'very beautiful',
               }
  #获取长度            
  print len(dictionary)
  #获取key的列表
  print dictionary.keys()
  #获取value的列表
  print dictionary.values()
  #查询key是不是存在
  print dictionary.has_key('good') #True
  print dictionary.has_key('bad') #False
  print '----------------'
  #add
  dictionary['bad'] = "not very good"
  print dictionary
  #modify  修改
  dictionary['bad'] = "failing to reach an acceptable standard"
  print dictionary
  #delete
  del dictionary['none']
  print dictionary
  #遍历
  print '-----遍历------'
  for key in dictionary.keys():
  	print key
  	print dictionary[key]
  # get value
  print '------get value------'
  print dictionary['bad']
  if dictionary.has_key('none'):
  	print dictionary['none']
  else:
  	print '没有这个key'

  print '---------homework2----------'

def homework2():
  dictionary2 = {
  				'abandon': 'to give up to the control or influence of another person or agent',
				'abase' :  'to lower in rank, office, prestige, or esteem ',
 				'abash' : 'to destroy the self-possession or self-confidence of '
  				}
  print dictionary2
  print '老爸先查了一个单词 etiquette'
  if dictionary2.has_key('etiquette'):
  	print dictionary2['etiquette']
  else:
  	print "没有查到,老爸怒了，把含有 'abandon' 一页的单词撕掉了"

  print "然后老爸又查了一个单词 'abase'"
  if dictionary2.has_key('abase'):
  	print "%s,老爸很开心，又把 'abandon' 加到字典里" % (dictionary2['abase'])
  else:
  	print "老爸很绝望"

if __name__ == '__main__':
  homework1()
  homework2()