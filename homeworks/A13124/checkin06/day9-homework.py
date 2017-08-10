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
  dictionary = {
                'good':'of a favorable character or tendenc',
                'none': 'not any such thing or person',
                'nice': 'very beautiful'
               }
  print len(dictionary)
  print dictionary.keys()
  print dictionary.values()
  print dictionary.has_key('good')
  dictionary['bad'] = 'not very good'
  dictionary['bad'] = 'not good'
  print dictionary
  del dictionary['bad']

  print dictionary['good']
  if dictionary.has_key('bad'):
  	print dictionary['bad']
  else:
  	print '没有bad这个单词'

  for key in dictionary:
  	print key
  	print dictionary[key]

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老爸在看一本英文书'
  if not book.has_key('etiquette'):
    print '老爸没有查到 %s ' % ('etiquette')

    del book['abandon']
    print '老爸撕掉了 %s ' % ('abandon')

    if book.has_key('abase'):
      print '老爸查到了 %s : %s' % ('abase', book['abase'])
      book['abandon'] = 'to give up to the control or influence of another person or agent'
      print '老爸把 %s 又加入到了字典里' % ('abandon')

    else:
      print '老爸没有查到 %s ' % (abase) 
  else:
    print '老爸查到了 %s '% ('etiquette')


if __name__ == '__main__':
  homework1()
  homework2()