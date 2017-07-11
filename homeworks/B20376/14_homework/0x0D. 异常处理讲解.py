#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

def homework1():
	week_overnight = [False,False,True,False,False] #周一到周五的情况

	for index,is_overnight in enumerate(week_overnight):
		print '今天星期 %d' %(index + 1)
		try:
			overnight_check(is_overnight)
		except Exception,e:
			# 发生错误的情况
			print '发生错误: %s' %(e)
		else:
			# 没有发生错误的情况
			print '附带脚本'

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'


def homework2():
	print '================='
	
	year_stayinJapan = [True,True,True,False,True]

	for index,is_stayinJapan in enumerate(year_stayinJapan):
		print '今年是 %d 年' %(index + 2012)
		try:
			stayinJapan_check(is_stayinJapan)
		except Exception,e:
			print '发生错误：%s' %(e)
		else:
			print 'Yeppy'


def stayinJapan_check(is_stayinJapan):
	if is_stayinJapan:
		print 'He came home for New Year'
	else:
		raise Exception('He could not come home for New Year this year')
	

if __name__ == '__main__':
	homework1()
	homework2()