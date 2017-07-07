#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
	week_overnight = [False,False,True,False,False] #列表周一到周五的情况
	for index,is_overnight in enumerate(week_overnight):
		print '今天星期%d' % (index +1)
		try:
			overnight_check(is_overnight)
		except Exception as e:
			print '发生错误：%s' % (e)



def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'

if __name__ == '__main__':
	main()