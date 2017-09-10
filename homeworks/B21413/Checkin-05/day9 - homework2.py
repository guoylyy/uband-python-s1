#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 190

def main():
	print '老爸在看一本英文书，他旁边有一个词典'

	dictionary = {
					'abandon': 'to give up to the control of influence of another person or agent',
					'abase': 'to lower in rank,office, prestige, or esteem',
					'absh': 'to destroy the self-possession or self-confidence of'
					}

	print '里面只有 %s 三个词' % dictionary.keys()

	print '老爸想从里面再找etiquette这个单词'
	if dictionary.has_key('etiquette'):
		print '老爸如愿以偿'
	else:
		print '老爸没有查到'

	print '老爸怒了'
	del dictionary ['abandon']
	print '他把含有abandon的一页撕掉了，现在里面只剩下 %s 两个词了' % dictionary.keys()

	print '老爸又开始查词abase'
	if dictionary.has_key('abase'):
		print '结果得到了解释'
	else:
		print '老爸暴走，撕爆整本字典'

	dictionary['abandon'] = 'to give up to the control of influence of another person or agent'

	print '老爸一开心，又把abandon加入了字典里，这下里面又回到  %s 三个单词了' % dictionary.keys()


if __name__ == '__main__':
  main()