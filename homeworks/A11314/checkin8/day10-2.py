#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 青牙

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码 7
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码 
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词

def homework1():
	key1="abase"
	value1="to lower in rank, office, prestige, or esteem"
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }

	print "老妈正在看一本英文书"

	if not book.has_key('etiquette'):
		print "老妈没有查到 %s 的意思" %('etiquette')
		del book[key1]
		print '老妈撕毁了 %s 的页面' % (key1)

		if book.has_key('abandon'):
			print "老妈查到了%s 的意思" %('abandon')
			book[key1]= value1
			print "老妈把 %s 的字典页又贴上了"% (key1)
		else:
			print "老妈没有找到了%s的意思" %('abandon')
	else:
		print "老妈查到了%s" %("etiquette")

	if book.has_key('abase'):
		print "老妈查到了%s：%s" %('abase',book['abase'])
	else:
		print "老妈没有查到%s" %('abase')
	if book.has_key('abash'):
		print "老妈查到了%s：%s" %('abash',book['abash'])
	else:
		print "老妈没有查到%s" %('abash')

if __name__ == '__main__':
	homework1()
	