#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan


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
                 'none':'not any such thing or person',
                 'nice':'very beautiful'
                }
  #长度
  print len(dictionary)

  #获得keys---.keys相当于获得key的列表
  print dictionary.keys()

  #获得values的列表
  print dictionary.values()

  #是不是在
  print dictionary.has_key('good')#有
  print dictionary.has_key('bad')#没有

  #add
  dictionary['bad'] = 'not very good'
  print dictionary
  print len(dictionary)

  #修改
  dictionary['bad'] = "failing to reach an acceptable standard"
  print dictionary

  #删除
  del dictionary['bad']
  print dictionary
  print len(dictionary)

  #取值 get value
  print '------'
  print dictionary['good']
  if dictionary.has_key('bad'): #这里注意要用圆括号不是方括号
  	print dictionary['bad']#这一段没有执行
  else:
  	print '没有 bad 这个单词'
  print '----------'

  #iterator
  for key in dictionary.keys():
  	print key
  	print dictionary[key] #提取key的值

def homework2():
    dictionary = {
                 'abandon':'to give up the control or influence of another person or agent',
                 'abase':'to lower in rank, office, prestige, or esteem',
                 'abash':'to destroy the self-possession or self-confidence of'
                }
    print '老爸今天心血来潮，想看英文小说！'
    print '老爸看到了一个单词，想查字典，结果发现：'

    if dictionary.has_key('etiquette'):
    	print dictionary['etiquette']
    else:
    	print '没有etiquette这个单词'
    	print '老爸很生气，把含有"abandon"一页的单词撕掉了,于是字典变成了这样：'
    	del dictionary['abandon']
    	print dictionary

    print '老爸又看到了一个单词，查字典发现：'

    if dictionary.has_key('abase'):
    	print 'abase: %s' % (dictionary['abase'])
    	print '老爸很开心，又把字典恢复原样，于是字典又变成了这样：'
    	dictionary['abandon'] = 'to give up the control or influence of another person or agent'
    	print dictionary
    else:
    	print '没有abase这个单词'


if __name__ == '__main__':
  homework2()