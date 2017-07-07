#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY
def main():
	week_overnight = [False, False, True, False, False]#周一到周五的情况
	for index, is_overnight in enumerate(week_overnight):
		print '今天星期%d ' % (index + 1)

		try:
			overnight_check(is_overnight)  #运行别的代码
		except Exception as e:
			print '发生错误：%s' % (e)  #如果在try部份引发了'name'异常
			print '老妈骂了老爸一顿，然后原谅了他'
		else: 
			print '附带脚本'  #如果没有异常执行这块代码
	pass

def overnight_check(is_overnight): 
	if is_overnight:
		raise Exception('离婚') #raise引发一个你定义的异常
	else:
		print '正常'

if __name__ == '__main__':
	main()