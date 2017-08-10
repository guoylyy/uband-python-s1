#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight=[False,False,True,False,False]#周一到周五
	for index,is_overnight in enumerate(week_overnight):
		print '今天星期%s'%(index+1)
		try:
			overnight_check(is_overnight)
			print '111'
		except Exception,e:
			#发生错误的情况
			print '发生错误：%s'%(e)
			print '老妈骂了老爸一顿，然后原谅了他'
		else:
			#没有发生错误的情况
			print '附带脚本'	
#func,离婚处理程序
#如果老爸夜不归宿
#启动离婚程序
def overnight_check(is_overnight):
	if is_overnight:
		#print '离婚'
		raise Exception('离婚')#强行中断程序的语法
	else:
		print '正常'



if __name__ == '__main__':
	main()