#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

def main():
	good1 = '大白菜'
	good2 = '空心菜'
	good3 = '花菜'
	good4 = '生姜'
	good5 = '小龙虾'

	#。。。。省略掉100个
	good100 = '蚌壳'

	print '老妈看到了 %s ' % (good1)
	print '老妈看到了 %s ' % (good2)
	print '老妈看到了 %s ' % (good1)
	print '老妈看到了 %s ' % (good2)
	print '老妈看到了 %s ' % (good1)
	print '老妈看到了 %s ' % (good2)


def main2():
	goods = '大白菜，空心菜，花菜，生姜，小龙虾'
	print '老妈看到了 %s' %(goods)
	


def main3():
	lst = ['dabaicai','kongxincai','huacai','shengjiang','xiaolongxia']
	for lst_item in lst:
		print '老妈看到了 %s ' %(lst_item)


if __name__ == '__main__':
	main()
	main2()
	main3()