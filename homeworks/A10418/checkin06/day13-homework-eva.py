#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	work_overnight = [False, False, True, False, False]
	for index, is_overnight in enumerate(work_overnight):
		print '今天星期%d'%(index+1)

		try:
			overnight_check(is_overnight)
		except Exception,e:
		#发生错误的情况
			print '发生错误：%s' %(e)
			print '老妈骂老爸一顿，然后原谅了他'
		else:
			print '附带脚本'

# func, 离婚处理程序
# 如果老爸夜不归宿
# 启动离婚程序

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'

if __name__ == '__main__':
	main()

