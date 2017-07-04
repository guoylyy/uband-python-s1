#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY


def main():
	dictionary = {
		'abandon': 'to give up to the control or influence of another person or agent', #忘记逗号 着重 标记
		'abase': 'to lower in rank, office, prestige, or esteem',
		'abash': 'to destroy the self-possession or self-confidence of'
	}
	print ' 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释'
	# 老爸先查了一个单词 'etiquette' 没有查到
	if dictionary.has_key('etiquette'):
		print "老爸查到[abandon]的意思是", dictionary['etiquette']
	else:
		print '老爸先查了一个单词  %s 没有查到' % ('etiquette')
		del  dictionary['abandon']
		print '老爸怒了，把含有 %s 一页的单词撕掉了' % ('abandon')
		#print dictionary

	# 然后老爸又差了一个单词 'abase' 得到了解释
	if dictionary.has_key('abase'):
		print "老爸又查到 %s 的意思是" % ('abase'), dictionary['abase']
	else:
		print '老爸再查了一个单词 "abase" 还是没有查到'

	# 老爸很开心，有把 'abandon' 加入到了字典里
	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print '老爸很开心，把 %s 加入到字典里' % ('abandon')
	#print dictionary


if __name__ == '__main__':
		main()	