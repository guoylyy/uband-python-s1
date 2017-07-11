#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera


def homework():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	who = 'Mom'
	print '%s is reading an English book.' % (who)
	if not book.has_key('etiquette'): #没有查到
		print "%s does not find %s" % (who, 'etiquette')
		del book['abase']    
		print "%s tears the page of %s."  % (who, 'abase')

		if book.has_key('abandon'):
			print '%s finds %s : %s' % (who, 'abandon', book['abandon'])

			book['abase'] = "to lower in rank, office, prestige, or esteem"
			print '%s adds the page of %s.' % (who, 'abase')
		else:
			print '%s does not find  %s ' % (who, 'abase') 
	else:
		print '%s finds %s. '% (who, 'etiquette')

	if book.has_key('abash'):
		print '%s finds %s: %s '% (who, 'abash', book['abash'])
	if book.has_key('abase'):
		print '%s finds %s: %s '% (who, 'abase', book['abase'])

 

if __name__ == '__main__':
	homework()							