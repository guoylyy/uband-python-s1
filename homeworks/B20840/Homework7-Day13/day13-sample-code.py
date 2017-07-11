#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author:B20840

def main():
	week_overnight = [False, False,True,False,False] #周一到周五的情况

	for index,is_overnight in enumerate(week_overnight):
		print '今天星期%d' %(index+1)
		try:
			overnight_check(is_overnight)
		except Exception, e:
			#print e
			print '发生错误：%s' %(e)
		else:
			#没有发生错误的情况
			print '附带脚本'

#func,离婚处理程序
#如果老爸夜不归宿
#就启动离婚程序
def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'
	


if __name__ == '__main__':
	main()