#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:lightningLUO

def main():
	week_homework = [True, False, True, True, False, True, True] #一周作业完成情况
	for index, accomplished in enumerate(week_homework):
		print '今天星期%d' %(index+1)

		try:
			homework_check(accomplished)
		except Exception,e:
			print '未完成作业:%s' % (e)

def homework_check(accomplished):
	if not accomplished:
		raise Exception('警告')
	else:
		print '打卡完成'


if __name__ == '__main__':
	main()