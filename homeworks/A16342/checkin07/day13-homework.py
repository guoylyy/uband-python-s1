#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

def main():
	week_overnight = [False, False, True, False, False]
	for index,is_overnight in enumerate(week_overnight):
		print '今天星期%d' % (index + 1)
		try:
			overnight_check(is_overnight)
		except Exception,e:
			print '发生错误：%s' % (e)
		else:
			print '附带脚本'

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'

def main2():
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	print '老妈来到菜市场'
	for index,lst_item in enumerate(lst):
		print '老妈看到了%s' %(lst_item)
		try:
			buy_check(index)
		except Exception,e:
			print '%s' % (e)
		else:
			print '买了%d斤' %  (index+1)
		print '老妈继续逛'

def buy_check(index):
	if index % 2 != 0:
		raise Exception('不买')


if __name__ == '__main__':
	main()
	main2()