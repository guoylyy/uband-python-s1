#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

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

def main():
	
	dictionary = {
					'abandon':'to give up to the control or influence of another person or agent',
					'abase':'to lower in rank, office, prestige, or esteem',
					'abash':'to destroy the self-possession or self-confidence of'
					}
	print '老爸查字典，字典里有'
	print dictionary

	if dictionary.has_key('etiquette'):
		print '老爸很满意'
	else:
		del dictionary['abandon']
		print '老爸怒了，撕掉了abandon那一页'
		print len(dictionary)
		print dictionary

	print '老爸继续查词abase得到了解释：'
	print dictionary['abase']

	print '老爸开心啦，把abandon那页粘了回去，现在的字典是：'
	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print dictionary




if __name__ == '__main__':
	main()