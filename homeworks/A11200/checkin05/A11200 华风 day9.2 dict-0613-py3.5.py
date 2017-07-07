#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

#作业2: 模拟下面的过程，用今天学到的知识
#【场景模拟】
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里
# 
def homework2():
  dictionary = {
                'abandon':'to give up to the control or influence of another person or agent',
                'abase':'to lower in rank, office, prestige, or esteem',
                'abash':'to destroy the self-possession or self-confidence of'
               }
  words = 'abase'
  words_no = 'etiquette'

  print ('老爸在看一本英文书，他旁边有一本词典，但只有三个单词的解释，如下：')
  print (dictionary)

  print ('老爸开始查字典，他想找‘etiquette’这个单词')
  if ('etiquette' in dictionary.keys()):
    print ('dictionary has %s' % (words_no))
  else :
  	del dictionary['abandon']

  print ('结果老爸没找到‘etiquette’这个单词，他把有‘abandon’这个单词的这页斯掉了')
  print (dictionary)

  print ('老爸又开始查字典，他想找‘abase’这个单词')
  if ('abase' in dictionary.keys()):
    print ('dictionary has %s' % (words))
    dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
  else :
  	pass
  
  print ('结果老爸找到了‘abase’这个单词，他又把‘abandon’这个单词加到字典中了')
  print (dictionary)

if __name__ == '__main__':
  homework2()