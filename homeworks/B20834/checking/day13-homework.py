#!/usr/bin/python
# -*- coding: utf-8 -*-

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('有点慌')
	else:
		print '正常'

def main():
	week_overnight = [False,False,True,False,False]
	for index,is_overnight in enumerate(week_overnight):
		print '今天星期%d' % (index + 1)
		try:
			overnight_check(is_overnight)
		except Exception as e :
			print '这是一个错误:%s' % (e)
		else:
			print '运行正常'
		
	
if __name__ == '__main__':
  main()
  
