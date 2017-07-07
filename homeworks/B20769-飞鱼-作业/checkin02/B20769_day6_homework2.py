#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

def print_lst(lst3) : #自定义一个函数，用以输出阵列
    for lst_item in lst3 :
    	print lst_item

def main():
	lst1 = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺','生菜','西瓜','苹果']
	lst2 = [2,2,3,50,20,10,3,8,40,15,1,4,6]
	length = len(lst1)
	total = 0
	print '今天菜市场有 %d 种菜，分别是： ' % (length )
	print_lst(lst1)
	print '老妈来到了菜市场'
	for n in xrange(0,length):
		print '看到了 %s ，卖 %d 元一斤' % (lst1[n], lst2[n])
		m = n%2
		if m == 1 :
			print '老妈没有买；'
		else :
			buy_amount = n+1
			money = buy_amount * lst2[n]
			print '老妈买了 %d 斤，花了 %d 元；' % (buy_amount , money)
			total = total + money
	print '老妈今天买菜总共花了 %d 元钱' % (total)
if __name__ == '__main__':
	main()
