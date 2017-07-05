#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

def main():
	pen_number=10
	pen_price=8.5
	pencil_number=5
	pencil_price=1

	#01. + - * / 练习
	pen_and_pencil_unit_price_sum=pen_price+pencil_price
	print 'pen and pencil unit price sum %g'%(pen_and_pencil_unit_price_sum)
	pen_and_pencil_unit_price_difference=pen_price-pencil_price
	print 'pen and pencil unit price difference %g'%(pen_and_pencil_unit_price_difference)
	pen_total_price=pen_price*pen_number
	print 'pen total price %0.2f'%(pen_total_price)
	pencil_total_price=pencil_price*pencil_number
	print 'pencil total price %0.2f'%(pencil_total_price)
	pen_unit_price=pen_total_price/pen_number
	print 'pen unit price %0.2f'%(pen_unit_price)
	pencil_unit_price=pencil_total_price/pencil_number
	print 'pencil unit price %0.2f'%(pencil_unit_price)

	#02. ** // % 练习
	number_1=3**4
	print '3的4次方 %g '%(number_1)
	number_2=10//3
	print '10除以3取整 %d '%(number_2)
	number_3=10%3
	print '10除以3的余数 %g '%(number_3)

	#03. & | 练习
	number_4=4&5
	print '4和5 按位与 %d '%(number_4)
	number_5=4|5
	print '4和5 按位或 %d '%(number_5)

	#04. > < >= <= 练习
	print 'test 1: %d' % (1 > 2)
	print 'test 2: %d' % (1 < 2)	
	print 'test 3: %d' % (3 >= 4)
	print 'test 4: %d' % (3 <= 4)
	#注：1为True，0为False

	#05. ==	!= 练习
	x=2
	y=3
	if x==y:
		print 'x等于y '
	if x!=y:
		print 'x不等于y '

	#06.not and or 练习
	a=3>5
	b=5>3
	if not a:
		print 'a为错 '
	if not b:
		print 'b为错 '

	if (a and b):
		print 'a和b都正确 '
	else :	
		print 'a和b中有错 '

	if (a or b):
		print 'a或b正确 '
	else :
		print 'a和b都错 '



if __name__ == '__main__':
  main()