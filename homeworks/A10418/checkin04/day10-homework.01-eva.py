#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
	book = {
			'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash':'to destory the self-possession or self-confidence of'
			}

	print '老爸在看一本英文书'

	if not book.has_key('etiquette'):
		print '老爸没有查到 %s 的意思'%('etiquette')

		del book['abandon']
		print '老爸撕毁了 %s 的页面'%('abandon')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s'%('abase',book['abase'])

			book['abandon']='to give up to the control or influence of another person or agent'
			print '老爸把 %s 的字典页又贴上了'%('abandon')

		else:
			print '老爸没有查到 %s '%('abase')
	else:
		print '老爸查到了 %s '%('etiquette')


def main01():
	book = {
			'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash':'to destory the self-possession or self-confidence of'
			}

	print '老妈在看一本英文书'

	if not book.has_key('etiquette'):
		print '老妈没有查到 %s 的意思'%('etiquette')

		del book['abandon']
		print '老妈撕毁了 %s 的页面'%('abandon')

		if book.has_key('abase'):
			print '老妈查到了 %s : %s'%('abase',book['abase'])

			book['abandon']='to give up to the control or influence of another person or agent'
			print '老妈把 %s 的字典页又贴上了'%('abandon')

		else:
			print '老妈没有查到 %s '%('abase')
	else:
		print '老妈查到了 %s '%('etiquette')

def main02():
	book = {
			'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash':'to destory the self-possession or self-confidence of'
			}

	print '老爸在看一本英文书'

	if not book.has_key('etiquette'):
		print '老爸没有查到 %s 的意思'%('etiquette')

		del book['abase']
		print '老爸撕毁了 %s 的页面'%('abase')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s'%('abase',book['abase'])

			book['abandon']='to give up to the control or influence of another person or agent'
			print '老爸把 %s 的字典页又贴上了'%('abandon')

		else:
			print '老爸没有查到 %s '%('abase')
	else:
		print '老爸查到了 %s '%('etiquette')	

def main03():
	book = {
			'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash':'to destory the self-possession or self-confidence of'
			}
	book2= book['abandon']
	
	print '老爸在看一本英文书'

	if not book.has_key('etiquette'):
		print '老爸没有查到 %s 的意思'%('etiquette')

		del book['abandon']
		print '老爸撕毁了 %s 的页面'%('abandon')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s'%('abase',book['abase'])

			book['abandon']=book2[0]
			print '老爸把 %s 的字典页又贴上了'%('abandon')

		else:
			print '老爸没有查到 %s '%('abase')
	else:
		print '老爸查到了 %s '%('etiquette')

	
def main04():
	book = {
			'abandon':'to give up to the control or influence of another person or agent',
			'abase':'to lower in rank, office, prestige, or esteem',
			'abash':'to destory the self-possession or self-confidence of'
			}
	book2= book['abandon']
	str = '然后把它打印出来了'
	print '老爸在看一本英文书'

	if not book.has_key('etiquette'):
		print '老爸没有查到 %s 的意思'%('etiquette')

		del book['abandon']
		print '老爸撕毁了 %s 的页面'%('abandon')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s'%('abase',book['abase'])
			print str


			book['abandon']=book2[0]
			print '老爸把 %s 的字典页又贴上了'%('abandon')

			if book.has_key('abash'):
				print '老爸查到了 %s : %s'%('abash',book['abash'])
				print str

			else:
				print '老爸没有查到 %s '%('abash')

		else:
			print '老爸没有查到 %s '%('abase')
	else:
		print '老爸查到了 %s '%('etiquette')


if __name__ == '__main__':
	main04()
