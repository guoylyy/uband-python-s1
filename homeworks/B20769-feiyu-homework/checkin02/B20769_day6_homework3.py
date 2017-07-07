#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

def print_lst(lst3) : #自定义一个函数，用以输出阵列
    for lst_item in lst3 :
    	print lst_item 

def main():
	lst1 = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	lst2 = [2,2,3,50,20,10,3,8,40,15]
	length1 = len(lst1)
	total = 0
	print '今天菜市场有 %d 种菜，分别是: ' % (length1)
	print_lst(lst1)
	lst11 = lst1[4:9]
	lst22 = lst2[4:9]
	print '老妈来到了菜市场,来到了1号台,看到了:'
	print_lst(lst11)
	length11 = len(lst11)
	for n in xrange(0,length11):
		print '看到了 %s ，卖 %d 元一斤' % (lst11[n], lst22[n])
		m = n%2
		if m == 1 :
			print '老妈没有买；'
		else :
			buy_amount = n+1
			money = buy_amount * lst22[n]
			print '老妈买了 %d 斤，花了 %d 元；' % (buy_amount , money)
			total = total + money
	print '老妈今天买菜总共花了 %d 元钱' % (total)
if __name__ == '__main__':
	main()
