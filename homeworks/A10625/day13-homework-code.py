#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################################两个作业写到一起了，就不截两张图了################
def main():
	week_overnight = [False, False, True, False, False]
	for index, is_overnight in enumerate (week_overnight):
		print '今天星期%d' % (index + 1)
		try:
			overnight_check(is_overnight)
		except Exception,e:
			print '发生错误：%s' % (e)
			print '老妈骂了老爸一顿，然后原谅了他'
		else:
			print '附带脚本'
	print '作业2'
	tup_1 = (1,2,3,4)
	try:
		del tup_1[0] 	 
	except Exception, e:
		print "发生错误：%s" % (e)
	a,b,c,d = (1,2,3,4) ### 这里做第十三天的题目
	print a
	print b
	print c
	print d
#可以不报错，不影响后面正确的语句的输出
def overnight_check (is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'
if __name__ == '__main__':
  main()