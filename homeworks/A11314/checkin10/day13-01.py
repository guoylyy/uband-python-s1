#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight=[False,False,True,False,False]
	for index,is_overnight in enumerate(week_overnight):
		print "今天星期%s，" %(index +1)
		try :
			over_check(is_overnight)
		except Exception,e:
			print "发生错误：%s" %(e)
			print "复合"
		else:
			print "附带……"


def over_check(is_overnight):
	if is_overnight:
		raise Exception("离婚")


if __name__ == '__main__':
	main()