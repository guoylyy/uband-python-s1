# -*- coding: utf-8 -*-
# @author: ashley

# Day2 - 
#        
# homework2


def main():
	orange_number = 5
	orange_price = 3.2
	egg_number = 12
	egg_price = 1.5

	orange_total_price = orange_price * orange_number
	egg_total_price = egg_price *egg_number

	print 'egg_cost %d ' % (egg_total_price)
	print 'egg_cost %g ' % (egg_total_price)
	print 'egg_cost %0.2f ' % (egg_total_price)

	number = 3**4
	print 'number = %d' % (number)
	print 'test: %d ' % (3 != 4)
	print 'test: %d ' % (3 >= 4)
	if 3:
		print 'good'
	if 0:
		print 'zzzz'
	if (3 != 3):
		print 'hahaha'

if __name__ == '__main__':
	  main()