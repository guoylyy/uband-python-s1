#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
	week_overnight=[True,True,False,True,True] #周一到周五的情况
	for index,week_item in enumerate(week_overnight):
		
		print "今天是星期%s"%(index+1)
		try:
			check(week_item)
		except Exception,e: #注意，这里的Exception是固定用法，首字母大写
			print "发生了错误"

def check(week_item):
	if not week_item:
		#print "放假"
		raise Exception('放假')#raise是什么意思？什么叫“强行中断程序的语法”？
		#根据菜鸟学院教程http://www.runoob.com/python/python-exceptions.html
		#raise的作用是自己触发异常，语句为：raise [Exception [, args [, traceback]]]
		#触发异常后，后面的代码就不再执行
	else:
		print "正常"
if __name__ == '__main__':
	main()