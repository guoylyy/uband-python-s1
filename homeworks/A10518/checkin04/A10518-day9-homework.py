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
 dictionary1 = {
              'haul':'to pull something heavy with a continuous, steady movement',
              'paramount':'more important than everything else',
              'secular':'not connectted with or controlled by a church or other religious authority'
              }

 print len(dictionary1)
 print dictionary1.keys()
 print dictionary1.values()
 print dictionary1.has_key('haul')
 print dictionary1.has_key('wow')
 dictionary1['bad'] = 'not very good'
 dictionary1['bad'] = 'failing to reach an acceptable standard'
 print dictionary1
 del dictionary1['bad']
 print dictionary1['paramount']
 if dictionary1.has_key('bad'):
  print dictionary1['bad']
 else:
  print '404 not found'
 for key in dictionary1.keys():
  print key
  print dictionary1[key]
  print '------------'

def homework2():
  dictionary = {
                'abandon':'to give up the control or influence of another person or agent',
                'abase':'to lower in rank, office, prestige, or esteem',
                'absh':'to destroy the self-possession or self-confidence of'
                }
  print dictionary.keys()
  print dictionary.values()
  print dictionary.has_key('etiquette')
  del dictionary['abandon']
  print dictionary['abase']
  dictionary['abandon'] = 'to give up the control or influence of another person or agent'


if __name__ == '__main__':
  homework1()
  homework2()
  