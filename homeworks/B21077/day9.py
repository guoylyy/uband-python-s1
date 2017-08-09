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
def main():
	print'dad is looking at an English book, he has a dictionary which only has the explanation of three word.'
	dictionary={
				'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem ',
				'abash':'to destroy the self-possession or self-confidence of'
				}
	#print dictionary.keys()#获得keys的列表
	#print dictionary.values()#获得values的列表
	for key in dictionary.keys():
		print key
		print dictionary[key]#获得列表与打印之后的没有任何关系。

	print'dad look up etiquette but cannot find it'
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']#这一段没有执行
	else:
		del dictionary['abandon']
		print"dad is angry，tear the page which has the word abandon"

	if dictionary.has_key('abase'):
		print 'dad look up another word abuse and have an explanation,he is happy and add abandon back to the dictionary'
		dictionary['abandon']="to give up to the control or influence of another person or agent"
	else:
		pass 
 
if __name__ == '__main__':
  main()