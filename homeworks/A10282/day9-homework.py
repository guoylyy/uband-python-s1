#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 233

#作业1:对照 day9 sample-code 打一遍代码
def homework1():
  dictionary = {
                'good':'of high quality or an acceptable standard', 
                'none':'not one of a group of people or things'
               }
#获得字典的长度
  print len(dictionary)
  print '-----------'
#获得key
  print dictionary.keys()
  print '-----------'
#获得value
  print dictionary.values()
  print '-----------'
#检测某个key是否存在
  print dictionary.has_key('good')
  print dictionary.has_key('bad')
  print '-----------'
#增加词典中的内容
  dictionary['bad'] = "of low quality or an unacceptable standard"
  print dictionary
  print len(dictionary)
  print '-----------'
#修改词典中的内容
  dictionary['bad'] = "failing to reach an acceptable standard"
  print dictionary
  print '-----------'
#删除词典中的内容
  del dictionary['bad']
  print dictionary
  print len(dictionary)
  print '-----------'
#获得某个value
  if dictionary.has_key('bad'):
  	print dictionary['bad']
  else:
  	print "单词 bad 不存在"
  print '-----------'
# for与词典结合 
  for key in dictionary.keys():
  	print dictionary[key]
  	print '----------------------------------'
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
  dictionary = {
                'abandan':'to give up to the control or influence of another person or agent',
                'absae':'to lower in rank, office, prestige, or esteem',
                'abase':'to destroy the self-possession or self-concidence of sth'
               }
  print "老爸先查了一个单词'etiquette'"
  if dictionary.has_key('etiquette'):
  	print dictionary['etiqutte']
  else:
  	print "没查到"
  	print "老爸怒了，把含有'abandan'一页的单词撕掉了"
  	del dictionary['abandan']
  	print dictionary
  	print len(dictionary)
  	print "然后老爸又查了一个单词'abase'"
  	print "得到了解释：" 
  	print dictionary['abase']
  	print "老爸很开心，又把'abandan'加入到了字典里"
  	dictionary['abandan'] = "to give up to the control or influence of another person or agent"
  	print dictionary
  	print len(dictionary)



if __name__ == '__main__':
  homework1()
  homework2()
