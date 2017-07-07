#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def overnightcheck(yes):
	if yes:
		raise Exception('离婚') 
	else:
		print "It's fine"

def main():
	week = [False, False, True, False, False]
	for index, yes in enumerate(week):
		print "今天星期%s" %(index + 1)
		try:
			overnightcheck(yes)
		except Exception,e:
			print "发生错误%s" %(e)
			print '老妈骂了老爸一顿，然后原谅了他'
		else:
			pass


if __name__ == '__main__':
	main()