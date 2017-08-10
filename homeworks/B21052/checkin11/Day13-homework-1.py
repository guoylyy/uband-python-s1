#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight = [False, False, True, False,False] #z周一到周五的情况
	for index, is_overnight in enumerate(week_overnight):
		print '今天星期 %s ' % (index + 1)
		try:
			overnight_check(is_overnight)
		except Exception, e:
			#发生错误的地方,继续走下去
			print '发生错误： %s' % (e)
			print '老妈骂了老爸一顿，然后原谅了他'
		else:
			#没有发生错误的地方
			print '附带脚本'

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'


if __name__ == '__main__':
  main()