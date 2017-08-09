#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def homework2():
	book = {
			"abandon": "to give up to the control or influence of another person or agent",
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	who = '老爸'
	tear_word = 'abandon' #可能会被撕毁的页的key
	print '%s在看一本英文书' % (who)
	
	if not book.has_key('etiquette'): #没有查到
		print '老妈没有查到 %s 的意思' % ('etiquette') #撕毁了abandon
		del book['abandon']
		print '老妈撕毁了 %s 的页面' % ('abase')
		if book.has_key('abase'):
			print '老妈查到了 %s : %s' % ('abase', book['abase'])
			book['abase'] = 'to lower in rank, office, prestige, or esteem' 
			print '老妈把 %s 的字典页又贴上了' % ('abase')
		else:
			print '老妈没有查到 %s ' % (abase) 
	else:
		print '老妈查到了 %s '% ('etiquette')
if __name__ == '__main__':
	homework2()