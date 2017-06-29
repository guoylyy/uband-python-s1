#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight_check = [False,False,True,False,False]
	for index,is_overnight in enumerate(week_overnight_check[1:4]):
		print '今天星期 %s' %(index + 1)

		try:
			overnight_check(is_overnight)
		except Exception as e:
			print '发生异常：%s' % (e)
		else:
			print '我是脚本'

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('是时候考虑下离婚了')
	else:
		print '正常'

if __name__ == '__main__':
	main()