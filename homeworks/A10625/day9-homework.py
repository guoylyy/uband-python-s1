#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业1:对照 day9 sample-code 打一遍代码



#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#

def homework1():
	print "-----------task one--------------"
	dictionary = { 'good' : 'of a favorable character or tendency',
					'none' : 'not any such thing or person',
					'nice': 'very beautiful'}
	
	#print dictionary
	#print dictionary['good']
	print len(dictionary)
	print dictionary.keys()#get all the keys ###注意， dictionary只有属性keys 没有属性key
	print dictionary.values() # get all the value. same as the keys. there is only "values" attribute, no "value" attribute
	print dictionary.has_key("good")# exist or not 
	print dictionary.has_key("bad")
	dictionary['bad'] = 'not that good'#adding new key and value
	print dictionary
	dictionary['bad'] = 'failing to reach an acceptable standard' # amending values
	print dictionary
	del dictionary['bad'] #delete 
	print dictionary
	print len(dictionary)
	print '--get value---'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print "can't find this word"
	print 'interator'
	for key in dictionary.keys():
		print key# print key
		print dictionary[key]#print value


def homework2():
	print 'homework 2'
	# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又差了一个单词 'abase' 得到了解释
# 老爸很开心，有把 'abandon' 加入到了字典里

	print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释 ' 
	dictionary = {'abandon' : 'to give up to the control or influence of another person or agent',
					'abase' : 'to lower in rank, office, prestige, or esteem ',
 					'abash' : 'to destroy the self-possession or self-confidence of '}
 	#for word in dictionary():
 		#print word# not callable
 	
 	print "老爸查了一个单词'etiquette'"
 	if dictionary.has_key('etiquette'):
 		print "老爸找到它了！然而这个都不会输出的其实"
 	else:
 		print '没有查到'
 		print "老爸怒了，把含有 'abandon' 一页的单词撕掉了"
 		del dictionary['abandon']
 		print "然后老爸又差了一个单词 'abase'"
 		if dictionary.has_key('abase'):
 			print "得到了解释"
 			print dictionary["abase"]
 			print "老爸很开心，又把 'abandon' 加入到了字典里"
 		else:
 			print '没有查到'
 			print "老爸怒了，买了个新的"
 		dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
 		print "length = %d" %  (len(dictionary))



if __name__ == '__main__':
  homework1()
  homework2()