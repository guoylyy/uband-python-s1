#!/usr/bin/python
#-*- coding: utf-8 -*-
# @author: Anna

def main():
	book = {
	        'abandon':'to give up to the control or influence of another person or agent',
            'abase':'to lower in rank, office, prestige, or esteem',
            'abash':'to destroy the self-possession or self-confidence of'
	        }
	print book
	
	print 'laoma1在看一本英文书'
	if not book.has_key('etiquette'):
		print 'laoma2没有查到 %s 的意思' % ('etiquette')

		del book['abandon']
		print 'laoma3撕毁了 %s 的页面' % ('abase') #1

		if book.has_key('abase'):
			print 'laoma4查到了 %s: %s ' % ('abase',book['abase'])

			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print 'laoma5把 %s 的字典页又贴上了' % ('abase') #2
		else:
			print 'laoma6没查到 %s ' % ('abase')
	else:
		print 'laoma8查到了 %s ' % ('etiquette')








if __name__ == '__main__':
	main()