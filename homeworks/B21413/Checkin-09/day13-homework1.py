#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight = [False, True, False, False, False] #包含判断的列表
	for index,is_overnight in enumerate(week_overnight): 
		print '今天星期%d' % (index + 1)

		try:
			check(is_overnight)
		except Exception,e:           #若没有这一段，就会出现报错。
			print '发生错误：%s' % (e)
			print '老妈骂了老爸一顿，然后当然选择原谅了他'
		else:
			print '又是平和的一天'

def check(is_overnight):
	if is_overnight:
		raise Exception('离婚') #中断程序，手动报错
	else:
		print '正常'

if __name__ == '__main__':
  main()