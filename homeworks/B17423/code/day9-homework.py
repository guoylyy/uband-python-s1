#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

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
  				'good' : 'of a favorable character or tendency',
  				'none' : 'not any such thing or person',
  				'nice' : 'very beautiful'
  				}

  #长度
  print (len(dictionary))

  #获得keys
  print (dictionary.keys())

  #获得values
  print (dictionary.values())

  #是不是在
  # print (dictionary.has_key('good'))  #python3不支持
  print ('good' in dictionary)
  print ('bad' in dictionary)

  #add
  dictionary['bad'] = 'not very good'
  print (dictionary)

  #modify
  dictionary['bad'] = 'failing to reach an acceptable standard'
  print (dictionary)

  #delete
  del dictionary['bad']
  print (dictionary)

  #get value
  print ('---get value---')
  print (dictionary['good'])
  if ('bad' in dictionary):
  	print (dictionary['bad'])
  else:
  	print ('没有bad这个单词')

  #iterator
  print ('---iterator---')
  #for key in dictionary.keys:  #python3不支持
  for key in dictionary:
  	print (key,':',dictionary[key])

def search_word(key, dict):
	if key in dict:
		print ("老爸查了一个单词%s，得到了解释" % key)
		return True
	else:
		print ("老爸查了一个单词%s，没有查到" % key)
		return False

def homework2():
  dict2 = {
  			'abandon' : 'to give up to the control or influence of another person or agent',
  			'abase' : 'to lower in rank, office, prestige, or esteem',
  			'abash' : 'to destroy the self-possession or self-confidence of'
  		  }

  print ('---homework 2---')
  print ('老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释')
  for key in dict2:
  	print (key,'“', dict2[key], "”")
  is_searched = search_word('etiquette',dict2)
  if (not is_searched):
  	del dict2['abandon']
  	print ("老爸怒了，把含有 'abandon' 一页的单词撕掉了")
  is_searched = search_word('abase', dict2)
  if is_searched:
  	dict2['abandon'] = 'to give up to the control or influence of another person or agent'
  	print ("老爸很开心，又把 'abandon' 加入到了字典里")

if __name__ == '__main__':
  homework1()
  homework2()