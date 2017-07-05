#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

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
	dictionary = {'abandon':'to give up to the control or influence of another person or agent',
                  'abase':'to lower in rank, office, prestige, or esteem',
                  'abash':'to destroy the self-possession or self-confidence of'
	             }

	length = len(dictionary)
	print '老爸在老爸在看一本英文书，他旁边有一个词典，字典里有 %d 个词的解释: ' % (length)
	print dictionary

	print "老爸先查了一个单词 'etiquette' "
	if dictionary.has_key('etiquette'):
		print '老爸得到了解释：'
		print dictionary['etiquette']
	else:
		print '没有查到。'

	del dictionary['abandon']
	print "老爸怒了，把含有 'abandon' 一页的单词撕掉了"
	length2 = len(dictionary)
	print '现在字典里还剩 %d 个词的解释：' % (length2)
	print dictionary

	print "老爸又查了一个单词 'abase' "
	if dictionary.has_key('abase'):
		print '老爸得到了解释：'
		print dictionary['abase']
	else:
		print '没有查到'

	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print "老爸很开心，又把 'abandon' 加入到了字典里"
	length3 = len(dictionary)
	print '现在字典里又是 %d 个词的解释：' % (length3)
	print dictionary



if __name__ == '__main__':
  main()