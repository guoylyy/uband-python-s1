#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

#sublime输出不全qaq 试过是对的

def homework2():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	print '老爸在看一本英文书'
	if not book.has_key('etiquette'): #没有查到
		print '老爸没有查到 %s 的意思' % ('etiquette')

    	#撕毁了abandon
		del book['abandon']
		print '老爸撕毁了 %s 的页面' % ('abandon')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s' % ('abase', book['abase'])

			#老爸黏贴了abandon
			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print '老爸把 %s 的字典页又贴上了' % ('abandon')
		else:
			print '老爸没有查到 %s ' % ('abase') 
	else:
		print '老爸查到了 %s '% ('etiquette')


#1 改了七处
def homework21():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	print '老妈在看一本英文书'
	if not book.has_key('etiquette'): #没有查到
		print '老妈没有查到 %s 的意思' % ('etiquette')

    	#撕毁了abandon
		del book['abandon']
		print '老妈撕毁了 %s 的页面' % ('abandon')

		if book.has_key('abase'):
			print '老妈查到了 %s : %s' % ('abase', book['abase'])

			#黏贴了abandon
			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print '老妈把 %s 的字典页又贴上了' % ('abandon')
		else:
			print '老妈没有查到 %s ' % ('abase') 
	else:
		print '老妈查到了 %s '% ('etiquette')



#2 改了五处
def homework22():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	print '老爸在看一本英文书'
	if not book.has_key('etiquette'): #没有查到
		print '老爸没有查到 %s 的意思' % ('etiquette')

    	#撕毁了abase
		del book['abase']
		print '老爸撕毁了 %s 的页面' % ('abase')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s' % ('abase', book['abase'])

			#老爸黏贴了abandon
			book['abase'] = 'to lower in rank, office, prestige, or esteem'
			print '老爸把 %s 的字典页又贴上了' % ('abase')
		else:
			print '老爸没有查到 %s ' % ('abase') 
	else:
		print '老爸查到了 %s '% ('etiquette')

#3
def homework23():
	abandon_mean = 'to give up to the control or influence of another person or agent'
	abase_mean = 'to lower in rank, office, prestige, or esteem'
	abash_mean = 'to destroy the self-possession or self-confidence of'
	book = {
			"abandon": abandon_mean,
			"abase": abase_mean,
			"abash" : abash_mean
			}
	print '老爸在看一本英文书'
	if not book.has_key('etiquette'): #没有查到
		print '老爸没有查到 %s 的意思' % ('etiquette')

    	#撕毁了abandon
		del book['abandon']
		print '老爸撕毁了 %s 的页面' % ('abandon')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s' % ('abase', book['abase'])

			#老爸黏贴了abandon
			book['abandon'] = abandon_mean
			print '老爸把 %s 的字典页又贴上了' % ('abandon')
		else:
			print '老爸没有查到 %s ' % ('abase') 
	else:
		print '老爸查到了 %s '% ('etiquette')

#4 4个重复的打印代码
def homework24():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	print '老爸在看一本英文书'
	if not book.has_key('etiquette'): #没有查到
		print '老爸没有查到 %s 的意思' % ('etiquette')

    	#撕毁了abandon
		del book['abandon']
		print '老爸撕毁了 %s 的页面' % ('abandon')

		if book.has_key('abase'):
			print '老爸查到了 %s : %s' % ('abase', book['abase'])

			#老爸黏贴了abandon
			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print '老爸把 %s 的字典页又贴上了' % ('abandon')
			if book.has_key('abash'):
				print '老爸查到了 %s : %s' % ('abash', book['abash'])
				if book.has_key('abandon'):
					print '老爸查到了 %s : %s' % ('abandon', book['abandon'])
				else:
					print '老爸没有查到 %s ' % ('abandon') 
			else:
				print '老爸没有查到 %s ' % ('abash') 
		else:
			print '老爸没有查到 %s ' % ('abase') 	
	else:
		print '老爸查到了 %s '% ('etiquette', book['etiquette'])

if __name__ == '__main__':
	homework2()
	homework21()
	homework22()
	homework23()
	homework24()