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
def dictionary():
	dic1={'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash': 'to destroy the self-possession or self-confidence of'
		} #z注意这里，不要忘了所有字符都要加引号~
	return dic1 #记得要return词典方便后面调用
def lookup(dic1):
	lookupWord='etiquette'
	lookupWord_2='abase'
	print "老爸先查了一个单词 '%s' "%(lookupWord)
	if dic1.has_key(lookupWord):
		print "查到了"
	else:
		print "没有查到"
		angry(dic1)
		
	print "老爸又查了一个单词 '%s' "%(lookupWord_2)
	if dic1.has_key(lookupWord_2):
		print "查到了"
		happy(dic1)
	else:
		print "没有查到"
def angry(dic1):
	del dic1['abandon']
	print "老爸怒了，把含有 'abandon' 一页的单词撕掉了，现在字典里的单词只剩下了",dic1.keys()
def happy(dic1):
	dic1['abandon']="to give up to the control or influence of another person or agent"
	print "老爸很开心，有把 'abandon' 加入到了字典里,现在字典里的单词还有",dic1.keys()
def les(dic1):
	les1=dic1.keys()
	les2=dic1.values()
	print "老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释"
	print "三个单词分别为",les1
	print "三个单词的意思分别为",les2
def homework2():
	dic1=dictionary()  #这里要记得调用前面的词典
	les(dic1)
	lookup(dic1)



if __name__ == '__main__':
  homework2()