#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: test

def main():
	apple_num=5.15
	apple_price = 4.844
	pie_num=6
	pie_price = 6.7

	apple_total_price = apple_price * apple_num
	pie_total_price = pie_price * pie_num

	print "pie cost %d " %pie_total_price
	print "pie cost %g " %pie_total_price
	print "pie cost %0.2f " %pie_total_price

	print "apple cost %d " %apple_total_price
	print "apple cost %g " %apple_total_price
	print "apple cost %0.2f " %apple_total_price

	number = 3**2
	print "number = %g" %number

	print "test: %g" %(1+2)
	print "test: %d" % (2-1)
	print "test: %d" %(2*3)
	print "test: %d" %(3/2)
	print "test: %d" %(9//7)
	print "test: %d" %(8.9//5)
	print "test: %d" %(9%6)
	print "test: %d" %(2<<2)
	print "test: %d" %(11>>1)
	print "test: %d" %(5&3)
	print "test: %d" %(5|3)
	print "test: %d" %(5^3)

	if 33%2 < 5:
	 	print "33%2 < 5 is ture"
	if 33%2 > 0:
	 	print "33%2 > 0 is ture" 
	x=1
	y=2
	print x<y
	print x<=y
	print x>y
	print x>=y
	print x==y
	print x!=y
	
	if 3>0 and 4>1:
		print "3>0 and 4>1 is ture "
	if 4<8 or 3<0:
		print "4<8 or 3<0 is ture"


if __name__ == '__main__':
	main()