#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxh

#作业1:对照 day9 sample-code 打一遍代码
def homework1():
  electricity = {
  'I':'current',
  'U':'电压',
  'P':'功率'
  }

  print len(electricity)

  abbreviation = electricity.keys()
  print abbreviation

  meaning = electricity.values()
  print meaning

  print electricity.values()

  print electricity.has_key('I')
  print electricity.has_key('K')

  electricity['R'] = 'resistance'
  print electricity

  del electricity['P']
  print electricity

  print electricity['I']

  for key in electricity.keys():
    print key
    print electricity[key]

if __name__ == '__main__':
  homework1()

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

def homework2():
  dictionary = {
  'abandon':'to give up to the control or influence of another person or agent',
  'abase': 'to lower in rank, office, prestige, or esteem',
  'abash': 'to destroy the self-possession or self-confidence of'
  }
  
  print dictionary.keys()

  if dictionary.has_key('etiquette') == False:
    print "老爸没查到 'etiquette'，怒了"
    del dictionary['abandon']
    print dictionary.keys()

  if dictionary.has_key('abase'):
    print "老爸查到'abase'，很开心"
    dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
    print  dictionary.keys()


if __name__ == '__main__':
  homework2()