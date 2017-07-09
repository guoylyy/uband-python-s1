#!/usr/bin/python
# -*- coding: utf-8 -*-

def homework2():
	book = {
			'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash':'to destroy the self-possession or self-confidence of'
			}

	print '老妈在看一本英文书'
	if not book.has_key('etiquette'):
		print '老妈没有查到%s的意思' %('etiquette')

		del book['abandon']
		print '老妈撕毁了%s的页面' %('abandon')
		if book.has_key('abase'):
			print '老妈查到了%s：%s' %('abase', book['abase'])
			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print '老妈把%s的字典页又贴上了' %('abandon')
		else:
			print '老妈没有查到%s' %('abase')
	else:
		print '老妈查到了%s' % ('etiquette')

if __name__ == '__main__':
	homework2()
