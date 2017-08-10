#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight = [False, False, True, False, False] #周一到周五的情况
 	
 	for index,is_overnight in enumerate(week_overnight):
 		print 'today is %d' %(index+1)
 		try:
 			overnight_check(is_overnight)
 		except Exception,e:
 			print 'error: %s' %(e)
 		else:
 			# no exception
 			print '附带脚本'


def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('divorce')
	else:
		print 'normal'

if __name__ == '__main__':
  main()