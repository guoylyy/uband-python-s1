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
  pass

def homework2(key3):
  dictionary = {
                'abandon': 'to give up to the control or influence of another person or agent',
                'abase': 'to lower in rank, office, prestige, or esteem ',
                'abash': 'to destroy the self-possession or self-confidence of '
               }
  list = ['etiquette','abase']
  print '老爸在看一本英文书 '
  for item in list:
    if dictionary.has_key(item)== False :
      del dictionary[key3]
      print "没查到'%s'" % item
      print "老爸怒了，把含'%s'一页的单词撕掉了 " %key3
    else: 
      dictionary[key3] = "to give up to the control or influence of another person or agent" 
      print "老爸查了个词:'%s'，得到了解释" % item
      print "老爸很开心，又把'%s'加入字典里" %key3




if __name__ == '__main__':
  homework2('abandon')