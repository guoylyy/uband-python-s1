#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight=[False,False,True,False,False]
	for index,is_overnight in enumerate(week_overnight):
		print '今天是第%d天'%(index+1)
		try:
			over_check(is_overnight)
		except Exception,e:
			print '发生错误%s'%(e)

	


def over_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'
if __name__ == '__main__':
	main()