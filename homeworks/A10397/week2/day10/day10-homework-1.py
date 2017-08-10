#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里

def homework():
	print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释 '

	dictionary = {'abandon':'to give up to the control or influence of another person or agent',
                  'abase':'to lower in rank, office, prestige, or esteem',
                  'abash':'to destroy the self-possession or self-confidence of'
                  }
	word1 = 'etiquette'
	print "老爸先查了一个单词 %s " % (word1)
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']
	else:
		print '没有查到'
	print '----------'

	word2 = 'abandon'
	print '老爸怒了，把含有 %s 一页的单词撕掉了' % (word2)
	del dictionary['abandon']
	print dictionary
	print '----------'

	word3 = 'abase'
	print '然后老爸又查了一个单词 %s 得到了解释' % (word3)
	print dictionary['abase']
	print '---------'

	print '老爸很开心，又把 %s 粘回到了字典里' % (word2)
	dictionary['abandon'] ='to give up to the control or influence of another person or agent'
	print dictionary


if __name__ == '__main__':
	homework()