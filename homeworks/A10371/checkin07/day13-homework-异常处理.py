#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi

def main():
  week_overnight = [False, False, True, False, False] #周一到周五的情况
  for index,is_overnight in enumerate(week_overnight):
  	print '今天星期%d' % (index + 1)

  	try:
  		overnight_check(is_overnight)
  	except Exception as e:
  		print '发生错误：%s' % (e)
  		print '老妈臭骂老爸，然后当然是原谅他'
  	else:
  		print '附带脚本'
  	
#func.离婚处理程序
#如果老爸夜不归宿
#启动离婚程序
def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')#强行中断的语法
	else:
		print '正常'

if __name__ == '__main__':
	main()