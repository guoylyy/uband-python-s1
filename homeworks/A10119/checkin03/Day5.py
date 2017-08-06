#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan


#lst是一个列表结构，用[]来囊括所有需要的变量或名单
#for语句是一个循环语句结构，可以用来调用lst的所有变量，在有很多数据要处理的时候会用到，比如名单、数据。


def main():
	good1 = '大白菜'
	good2 = '空心菜'
	#............省略1001个
	good100 = '蚌壳'

	print '老妈看到了 %s '% (good1)
	print '老妈看到了 %s '% (good2)
	print '老妈看到了 %s '% (good100)

def main2():
	goods = '大白菜， 空心菜， 花菜， 生姜， 小龙虾 '

	print '老妈看到了 %s ' %(goods)

def main3():
	print '---------------'
	lst = ['大白菜', '空心菜', '花菜', '生姜', '小龙虾']#列表
	for lst_item in lst:  #遍历
		print '老妈看到了 %s' % (lst_item)

if __name__ == '__main__':
		main()
		main2()
		main3()