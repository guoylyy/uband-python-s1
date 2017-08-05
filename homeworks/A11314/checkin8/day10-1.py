#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 青牙

def homework1():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	print "老爸正在看一本英文书"

	if not book.has_key('etiquette'):
		print "老爸没有查到 %s 的意思" %('etiquette')
		del book['abandon']
		print '老爸撕毁了 %s 的页面' % ('abandon')

		if book.has_key('abase'):
			print "老爸查到了%s 的意思" %('abase')
			book['abandon']="to give up to the control or influence of another person or agent"
			print "老爸把 %s 的字典页又贴上了"% ('abandon')
		else:
			print "老爸找到了%s的意思" %('abase')
	else:
		print "老爸查到了%s" %("etiquette")


if __name__ == '__main__':
	homework1()
	