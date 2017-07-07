#!/usr/bin/python
#-*- coding:utf-8 -*-
#@author:SKY

def homework():
	book={
	'abandon':'to give up to the control or influence of another person or agent',
	'abase':'to lower in rank ,office, prestige, or esteem',
	'abash':'tto destroy the self-possession or self-confidence of '
	}
	print ' 老爸在看一本英文书 '
	try:
		if not book.has_key('etiquette'):
			print ' 老爸没有查到 %s 的意思 '% ('etiquette')

			del book['abandon']
			print  ' 老爸撕毁了 %d 的页面 ' % ('abandon')

			if book.has_key('abase'):
				print  ' 老爸查到了 %s : %s ' % ('abase',book['abase'])

				book['abandon']='to give up to the control or influence of another person or agent'
				print  ' 老爸把 %s 的字典页又贴上了 ' %('abandon')

			else:
				print ' 老爸没有查到 %s ' % ('abase')
		else:
			print ' 老爸查到了 %s ' % ('etiquette')
	except Exception,e:
		print '捕获异常：%s ' %(e) 

if __name__ == '__main__':
	homework()