#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def homework2():
	dictionary = {'abandon':'to give up to the control or influence of another person or agent',
				  'abase':'to lower in rank, office, prestige, or esteem',
				  'abash':'to destroy the self-possession or self-confidence of'
				  }

	who = 'father'

	print 'One day, %s was reading an Englsih book while a dictionary with only three words was besides him.'  % (who)
	print '%s found a  unknown word, etiquette, then he looked it up in that dictionary.' % (who)

	if dictionary.has_key('etiquette'):  
		print dictionary['etiqutte']  #没有这个单词则不执行此操作
	else:
		print 'He did not found it in the dictionary.'

	# if not dictionary.has_key('etiquette'): 没有查到
	#	print 'He did not found it in the dictionary.'

	#撕毁了abandon这一页
	del dictionary['abandon']
	print "%s got angry, then he teared off that page with the word %s on." % (who,'abandon')

	if dictionary.has_key('abase'):
		print '%s found %s: %s' % (who, 'abase', dictionary['abase'])
		
	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print '%s felt happy and pasted back that page with the word %s on' % (who,'abandon')

if __name__ == '__main__':
  homework2()