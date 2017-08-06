def main():
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price

	print 'pie cost %d' % (pie_total_price)
	print 'pie cost %g' % (pie_total_price)
	print 'pie cost %0.2f' % (pie_total_price)

	number = 2**3
	print 'number = %d' % (number)

	#fu hao test
	x = 3.0
	y = 5
	number1 = x - y
	print number1
	number2 = y / x
	print number2
	number3 = y // x
	print number3
	number4 = y % x
	print number4

	print 'test: %d ' % (x<y)
	print 'test: %d ' % (x>=y)

	if not(x==y):
		print 'lalala'

	if (x!=y) and (x>=y):
		print 'wrong'

	if (x==y) or (x<=y):
		print '246'

if __name__ == '__main__':
  main()