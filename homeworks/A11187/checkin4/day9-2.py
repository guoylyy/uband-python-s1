#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui

def homework2():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": 'to lower in rank, office, prestige, or esteem',
			"abash": 'to destroy the self-possesion or self-confidence of'	
			}
	print 'father is reading an English book'
	if not book.has_key('etiquette'):
		print 'father does not find the meaning of %s ' % ('etiquette')

		del book['abandon']
		print 'father tears the page of  %s ' % ('abandon')

		if book.has_key('abase'):
			print 'father finds the meaning of  %s : %s' % ('abase', book['abase'])

			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print 'father pastes the page of  %s on the dictinary' % ('abandon')

		else:
			print 'father does not find %s' % ('etiquette')
	else:
		print 'father finds %s' % ('etiquette')

if __name__ == '__main__':
	homework2()