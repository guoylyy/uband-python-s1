#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	dictionary = {
	 "abandon": 'to give up to the control or influence of another person or agent',
	 "abase": "to lower in rank, office, prestige, or esteem",
	 "abash" : "to destroy the self-possession or self-confidence of"
	}
	print '老爸在看一本英文字典'
	# 老爸把字典翻了一遍
	#   - 看到%s（单词）:%s(意思)
	if not dictionary.has_key('etiquette'): #没有查到
		print '老爸没有查到 %s 的意思' % ('etiquette')

		#撕毁abandon
		del dictionary['abandon']
		print '老爸撕毁了 %s 的页面' % ('abandon')

		if dictionary.has_key('abase'):
			print '老爸查到了 %s: %s' % ('abase', dictionary['abase'])

			#老爸粘贴了代码
			dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
			print '老爸把 %s 的字典页面又贴上了' % ('abandon')

		else:
			print '老爸没有查到 %s' % ('abase')
	else:
		print '老爸查到了 %s' % ('etiquette')

if __name__ == '__main__':
	main()

