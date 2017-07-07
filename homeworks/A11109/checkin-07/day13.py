#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight = [False, False, True, False, False]
	for index, is_overhight in enumerate(week_overnight):
		print '今天星期 %d' % (index + 1)

		try:
			overnight_check(is_overhight)
		except Exception,e:
			print '发生错误： %s' % (e)
			print '老妈骂了老爸一顿，然后原谅了他'
		else:
			print '附带脚本'

def overnight_check(is_overhight):
	if is_overhight:
		raise Exception('离婚')
	else:
		print '正常'

if __name__ == '__main__':
  main()